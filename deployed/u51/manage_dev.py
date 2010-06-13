#!/usr/bin/env python
try:
	import settings_dev # Assumed to be in the same directory.
except ImportError:
	import sys
	sys.stderr.write("Error: Can't find the file 'settings_dev.py' in the directory containing %r. You might want to adjust your DJANGO_SETTINGS_MODULE environment variable.\n" % __file__)
	sys.exit(1)

if __name__ == "__main__":
	from django.core.management import execute_manager
	execute_manager(settings_dev)
