import os, sys
import django.core.handlers.wsgi

sys.path.append('/usr/lib/python2.5/site-packages/django')

sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), '..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'u51.settings'
application = django.core.handlers.wsgi.WSGIHandler()
