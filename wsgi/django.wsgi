import os, sys

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..')))

import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'u51.settings'
application = django.core.handlers.wsgi.WSGIHandler()
