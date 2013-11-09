#!/usr/bin/env python2
import sys
import json

# Usage:
#   python manage.py dumpdata | python u51-json-export.py

# JSON output from `python manage.py dumpdata`
data = json.loads(sys.stdin.read())

# Filter passwords from django DB dump
pws = [x['fields'] for x in data if x['model'] == 'pws.entry']

print json.dumps(pws, indent=4)
