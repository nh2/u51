def jquery(request):
	from django.conf import settings
	return {'JQUERY_URL': settings.JQUERY_URL}
