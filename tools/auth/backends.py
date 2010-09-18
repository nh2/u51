from django.conf import settings
from django.contrib.auth.models import User

class SingleUserBackend(object):
	"""
	Authenticate against only one user defined in settings.LOGIN_USER.
	"""
	def __init__(self, single_user_name=None):
		self.single_user_name = single_user_name or settings.LOGIN_USER

	def authenticate(self, password=None):
		user = self.get_or_create_single_user()
		pw_valid = user.check_password(password)
		return user if pw_valid else None

	def get_user(self, user_id):
		return self.get_or_create_single_user()

	def get_or_create_single_user(self):
		try:
			return User.objects.get(username=self.single_user_name)
		except User.DoesNotExist:
			# Create the single user and return it
			# to permit first login with an empty password.
			user = User(username=self.single_user_name)
			user.set_password('')
			user.save()
			return user

	def password_set(self):
		return not self.get_or_create_single_user().check_password('')
