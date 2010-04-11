def jquery(request):
	from django.conf import settings
	return {
		'JS_URL': settings.JS_URL,

		'JS_COPYTOCLIPBOARD': settings.JS_COPYTOCLIPBOARD,

		'JQ_URL': settings.JQ_URL,
		'JQ_JQ': settings.JQ_JQ,
		'JQ_QTIP': settings.JQ_QTIP,
		'JQ_UITABLEFILTER': settings.JQ_UITABLEFILTER,
		'JQ_TABLESORTER': settings.JQ_TABLESORTER,
		'JQ_HOVERINTENT': settings.JQ_HOVERINTENT,
		'JQ_UIEFFECTS': settings.JQ_UIEFFECTS,
	}
