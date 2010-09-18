from django.conf import settings
from u51.pws.AuthBackends import password_set

def all(request):
	return {
		'Media': settings.MEDIA,
		'password_set': password_set(),
	}
