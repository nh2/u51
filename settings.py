import os
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)

DEBUG = False  # Set to True for development ONLY (huge security risk for deployment)
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
	'localhost',
	'127.0.0.1',
]

ADMINS = [
	# ('Your Name', 'your_email@example.com'),
]

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', # Add 'django.db.backends.postgresql_psycopg2', 'django.db.backends.mysql', or 'django.db.backends.sqlite3'.
		                                        # see https://docs.djangoproject.com/en/dev/ref/settings/#databases
		'NAME': 'u51-test.db.sqlite3',          # Or path to database file if using sqlite3.
		'USER': 'u51',                      # Not used with sqlite3.
		'PASSWORD': '',                  # Not used with sqlite3.
		'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
	}
}

# THIS IS SECURITY CRITICAL
# ONLY SET THIS when behind an HTTPS proxy (e.g. nginx reverse proxy)
# that makes sure that 'HTTP_X_FORWARDED_PROTOCOL' is set
# on HTTPS connections and unset for HTTP connections.
# see https://docs.djangoproject.com/en/1.4/ref/settings/#secure-proxy-ssl-header
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

LOCALE_PATHS = [
	os.path.join(PROJECT_ROOT, 'locale'),
]

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [
	# Put strings here, like "/home/html/static" or "C:/www/django/static".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	os.path.join(PROJECT_ROOT, 'u51-static'),
]

# Load SECRET_KEY from file if not defined.
# See https://docs.djangoproject.com/en/2.2/ref/settings/#secret-key
try:
	SECRET_KEY
except NameError:
	from tools.key import get_generate_secret_key
	SECRET_KEY = get_generate_secret_key(PROJECT_ROOT)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
]

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
]

MIDDLEWARE = [
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	# Uncomment the next line for simple clickjacking protection:
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '%s.urls' % PROJECT_NAME

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'u51.wsgi.application'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
		'APP_DIRS': True,  # so that `pws`'s templates are loaded
		'OPTIONS': {
			'context_processors': [
				'pws.context_processors.all',
			],
		},
	}
]

INSTALLED_APPS = [
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# Uncomment the next line to enable the admin:
	# 'django.contrib.admin',
	# Uncomment the next line to enable admin documentation:
	# 'django.contrib.admindocs',

	'templatetag_sugar',

	'u51', # needed for JS translations (javascript_catalog)
	'pws',
]

TEMPLATE_CONTEXT_PROCESSORS = [
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.tz',
	'django.contrib.messages.context_processors.messages',
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
	}
}

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = [
	'tools.auth.backends.SingleUserBackend'
]

# for a simple one-user auth system
LOGIN_USER = 'user'

class MEDIA:
	JS_URL = os.path.join(STATIC_URL, 'js')

	JS_COPYTOCLIPBOARD = os.path.join(JS_URL, 'copytoclipboard.js')

	JQ_URL = os.path.join(JS_URL, 'jquery')
	JQ_JQ = os.path.join(JQ_URL, 'jquery-1.4.2.js')
	JQ_QTIP = os.path.join(JQ_URL, 'qtip', 'jquery.qtip-1.0.js')
	JQ_UITABLEFILTER = os.path.join(JQ_URL, 'uitablefilter', 'jquery.uitablefilter.mod.js')
	JQ_TABLESORTER = os.path.join(JQ_URL, 'tablesorter', 'jquery.tablesorter.js')
	JQ_HOVERINTENT = os.path.join(JQ_URL, 'hoverintent', 'jquery.hoverintent.js')
	JQ_UIEFFECTS = os.path.join(JQ_URL, 'ui', 'jquery.ui-1.8.effects-custom.js')
