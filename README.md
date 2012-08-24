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

Assuming you have a custom Django installation, run it with:

```
PYTHONPATH=/path/to/django:../ python manage.py runserver
```
