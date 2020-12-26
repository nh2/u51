u51
===

A web password manager to run on your private server.

Pull requests are much appreciated.


Install
-------

u51 runs on Django. Read the DEPENDENCIES file.

Then change the `settings.py` and adjust your settings (especially the database).

If you choose a DB driver like `postgresql_psycopg2`, make sure you have that driver installed.

Set `DEBUG = True` until it works, then MAKE SURE TO SET IT BACK OFF for security.


Running and updating
--------------------

You have to set the `PYTHONPATH` in order for u51 to find Django (and its own `settings.py`).

Initialize/update the database:

```
PYTHONPATH=/path/to/django/:vendor/django-templatetag-sugar/:../ python manage.py makemigrations pws
PYTHONPATH=/path/to/django/:vendor/django-templatetag-sugar/:../ python manage.py makemigrations
PYTHONPATH=/path/to/django/:vendor/django-templatetag-sugar/:../ python manage.py migrate
```

The above command may ask you to create users.
Say `yes` and choose `user` as the username.
The password you choose will be your login password.

Update static files using:

```
PYTHONPATH=/path/to/django/:vendor/django-templatetag-sugar/:../ python ./manage.py collectstatic
```

Then run the webserver with:

```
PYTHONPATH=/path/to/django/:vendor/django-templatetag-sugar/:../ python manage.py runserver
```

You need to set `DEBUG = True` for `runserver` to serve static files, or use `runserver --insecure`.

If you like it, deploy it on a real WSGI webserver, e.g. using Gunicorn, or nginx with uWSGI or Apache with mod-wsgi.

Do not forget that you have to do that in order to get SSL connections; **if you don't, everyone on the network will be able to read your passwords.** You can also run it locally only and use an SSH port forward, of course.

*And don't forget to set `DEBUG = False` once it runs!*


Security notice
---------------

If you make your u51 publicly accessible, your passwords are approximately as secure in u51 as Django is secure, at least until in-browser encryption is implemented. **Currently, passwords are saved in the database as clear text.**

Disclaimer: Although interested in making u51 as secure as possible, the authors of u51 take no responsibility for your data being exposed.


TODO
----

These are the features I would implement next:

* We have currently vendored [`vendor/django-templatetag-sugar`](https://github.com/alex/vendor/django-templatetag-sugar)
  in `vendor/django-templatetag-sugar/` because the project is unmaintained.
  and it needed some changes for u51 to upgrade to Django 2.2.
  We should check if it is still necessary at all or if there are better replacements.
* Simple deployment instructions for Gunicorn.
* A warning when using SQLite where the DB is created with read-all permissions.
* Replacing the filter by something that is not 1000 times slower than it should be.
* Using in-browser encryption with the login password.
