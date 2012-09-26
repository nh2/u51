u51
===

A web password manager.


Install
-------

u51 runs on Django. Read the DEPENDENCIES file.

Then change the `settings.py` and adjust your settings (especially the database).

If you choose a DB driver like `postgresql_psycopg2`, make sure you have that driver installed.

Set `DEBUG = True` until it works, then MAKE SURE TO SET IT BACK OFF for security.


Run
---

You have to set the `PYTHONPATH` in order for u51 to find Django (and it's own `settings.py`).

Initialize the database:

```
PYTHONPATH=/path/to/django:../ python manage.py syncdb
```

The above command will ask you to create users.
Say `yes` and choose `user` as the username.
The password you choose will be your login password.

Then run the webserver with:

```
PYTHONPATH=/path/to/django:../ python manage.py runserver
```

You need to set `DEBUG = True` for `runserver` to work.

If you like it, deploy it on a real WSGI webserver, e.g. using Gunicorn or Apache with mod-wsgi.

Do not forget that you have to do that in order to get SSL connections; **if you don't, everyone on the network will be able to read your passwords.** You can also run it locally only and use an SSH port forward, of course.

*And don't forget to set `DEBUG = False` once it runs!*
