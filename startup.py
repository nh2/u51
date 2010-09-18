"""
For a quick startup loading commonly used classes, installed apps, and console utils.

Usage: After manage.py shell, type 'from [this module] import *'.
"""

from django.conf import settings
from django.db import connection, models

# Load each installed app and put models into the global namespace.
for app in models.get_apps():
    exec("from %s import *" % app.__name__)

def last_query():
    "Show the last query performed."
    return connection.queries[-1]

#===================================================
# Add commonly used modules, classes, functions here
#===================================================
from django import forms
import os
from datetime import datetime

