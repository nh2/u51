from django.conf import settings
from django.contrib.auth.models import User

class SingleUserBackend:
	"""
	Authenticate against only one user defined in settings.LOGIN_USER.
	"""
	def authenticate(self, password=None):
		user = get_or_create_default_user()
		pw_valid = user.check_password(password)
		return user if pw_valid else None

	def get_user(self, user_id):
		return get_or_create_default_user()

def get_or_create_default_user():
	try:
		return User.objects.get(username=settings.LOGIN_USER)
	except User.DoesNotExist:
		# Create the LOGIN_USER and return it
		# to permit first login with an empty password.
		user = User(username=settings.LOGIN_USER)
		user.set_password('')
		user.save()
		return user

def password_set():
	return not get_or_create_default_user().check_password('')
