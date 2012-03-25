#!/usr/bin/env python
import os
import sys

try:
	import django
except ImportError:
	import sys
	sys.stderr.write("Error: Can't import Django. Make sure that it is on sys.path or specify PYTHONPATH=/path/to/django on shell invocation.\n")
	sys.exit(1)

if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "u51.settings")

	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)
