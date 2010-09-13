from django.utils import simplejson

def json_response(json):
	return HttpResponse(simplejson.dumps(json), mimetype='application/javascript')
