from django.conf import settings

def all(request):
	return {
		'Media': settings.MEDIA,
	}
