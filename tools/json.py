import json
from django.http import HttpResponse

def json_response(json_obj):
	return HttpResponse(json.dumps(json_obj), content_type='application/javascript')
