from django.conf import settings
from u51.tools.auth.backends import SingleUserBackend

def all(request):
	return {
		'Media': settings.MEDIA,
		'password_set': SingleUserBackend().password_set(),
	}
