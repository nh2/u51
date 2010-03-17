def jquery(request):
	from django.conf import settings
	return {
		'JQ_URL': settings.JQ_URL,
		'JQ_JQ': settings.JQ_JQ,
		'JQ_QTIP': settings.JQ_QTIP,
	}
