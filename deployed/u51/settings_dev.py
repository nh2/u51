import os
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	# ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(PROJECT_PATH, 'db_dev.sqlite')             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de-de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '(sd#o2hmvss272a&h9!a^dzb#1sis^_x24lby6q&rzb*)d^k33'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'u51.urls'

TEMPLATE_DIRS = (
	os.path.join(PROJECT_PATH, 'templates'),
	os.path.join(PROJECT_PATH, 'templates', 'pws'),
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',

	'u51.pws',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'pws.context_processors.jquery',
)

LOGIN_URL='/login/'
LOGIN_REDIRECT_URL='/'

AUTHENTICATION_BACKENDS = ('pws.AuthBackends.SingleBackend',)

# for a simple one-user auth system
LOGIN_USER='user'


JS_URL = os.path.join(MEDIA_URL, 'js')

JQ_URL = os.path.join(JS_URL, 'jquery')
JQ_JQ = os.path.join(JQ_URL, 'jquery-1.4.2.js')
JQ_QTIP = os.path.join(JQ_URL, 'qtip', 'jquery.qtip-1.0.js')
JQ_UITABLEFILTER = os.path.join(JQ_URL, 'uitablefilter', 'jquery.uitablefilter.mod.js')
JQ_TABLESORTER = os.path.join(JQ_URL, 'tablesorter', 'jquery.tablesorter.js')
JQ_HOVERINTENT = os.path.join(JQ_URL, 'hoverintent', 'jquery.hoverintent.js')
JQ_UIEFFECTS = os.path.join(JQ_URL, 'ui', 'jquery.ui-1.8.effects-custom.js')

JS_COPYTOCLIPBOARD = os.path.join(JS_URL, 'copytoclipboard.js')
