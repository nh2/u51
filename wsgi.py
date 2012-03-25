"""
WSGI config for u51 project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import sys
import os

# Assumed directory structure:
#
#     /path/to/somewhere/
#         django/
#             Django-1.4.x
#         u51/
#             pws/
#             settings.py

# For Apache with modwsgi, use:
#
#     WSGIScriptAlias / /path/to/somewhere/u51/wsgi.py
#
#     <Directory /path/to/somewhere/u51/>
#         <Files wsgi.py>
#             Order deny,allow
#             Allow from all
#         </Files>
#     </Directory>

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'django', 'Django-1.4.x')))
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "u51.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
