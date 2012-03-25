from settings import *
import sys, os, user

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(PROJECT_ROOT, 'db_dev.sqlite'),
	},
}
