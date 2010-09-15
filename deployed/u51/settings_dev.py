from settings import *
import sys, os, user

# Appending django do the end so that you can use another version via PYTHONPATH
sys.path.append(os.path.join(user.home,"src","django","django-1.2.x"))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(PROJECT_ROOT, 'db_dev.sqlite')
