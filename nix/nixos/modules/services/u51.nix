# u51
#
# This module requires initial manual setup using:
#
#     mkdir /var/u51/
#     cd /var/u51/
#     git clone https://github.com/nh2/u51 /var/u51/u51
#
# The DB is by default sqlite, and in the `secrets/` subdirectory,
# so that is where the state is.
{ config, lib, pkgs, ... }:
let
  cfg = config.services.u51;
in
with lib;
{
  options = {

    services.u51 = {

      enable = mkEnableOption "u51 service";

    };

  };

  config = mkIf cfg.enable {

    users.users.u51 = {
      group = config.users.groups.u51.name;
      isSystemUser = true;
      createHome = false;
    };
    users.groups.u51 = {};

    systemd.tmpfiles.rules = [
      # The `secrets/` directory (contains the sqlite DB and secret.key) shall
      # be readable/writable only by the u51 user. Django leaves no control
      # over the sqlite file permissions and creates it with `o+r`, which is
      # bad. Using parent dir permissions is a race-free solution.
      "d '/var/u51/u51/secrets' 0700 ${config.users.users.u51.name} ${config.users.users.u51.group} - -"
    ];

    systemd.services.u51 =
      let
        djangoEnv = pkgs.python3.withPackages (ps: with ps; [
          gunicorn
          django_2_2
        ]);
      in {
        description = "u51 password manager";
        after = [ "network.target" ];
        wantedBy = [ "multi-user.target" ];
        environment = {
          # So that the u51 sub-directory can be `import`ed, and vendored libs.
          PYTHONPATH = "/var/u51/:vendor/django-templatetag-sugar/";
        };
        serviceConfig = {
          WorkingDirectory = "/var/u51/u51/";
          ExecStartPre =
            let
              u51PermsScript = pkgs.writeShellScript "u51-perms" ''
                set -eu -o pipefail
                echo "Setting permissions"
                chown -R ${config.users.users.u51.name}:${config.users.users.u51.group} /var/u51/
              '';
              managepyScript = pkgs.writeShellScript "u51-managepy" ''
                set -eu -o pipefail
                echo "Running manage.py"
                ${djangoEnv}/bin/python manage.py makemigrations pws;
                ${djangoEnv}/bin/python manage.py makemigrations;
                ${djangoEnv}/bin/python manage.py migrate;
                ${djangoEnv}/bin/python manage.py collectstatic --no-input;
              '';
            in
               # '+' runs as root
              ''
                +${u51PermsScript} ; ${managepyScript}
              '';
          ExecStart = ''${djangoEnv}/bin/gunicorn \
            --access-logfile \
            - --workers 1 \
            --bind unix:/var/u51/gunicorn.sock \
            wsgi:application
          '';
          Restart = "always";
          RestartSec = "10s";
          User = config.users.users.u51.name;
        };
        unitConfig.StartLimitIntervalSec = 0; # ensure Restart=always is always honoured
      };

    services.nginx.virtualHosts = {
      "u51.new.deditus.de" = {
        enableACME = true;
        forceSSL = true;
        locations = {
          "/" = {
            proxyPass = "http://unix:/var/u51/gunicorn.sock";
          };
          "/static/" = {
            root = "/var/u51/u51";
          };
        };
      };
    };

  };
}
