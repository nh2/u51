from settings import *
import sys, os, user

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(PROJECT_ROOT, 'db_dev.sqlite')
