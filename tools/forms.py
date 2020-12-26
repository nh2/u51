from django import forms
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import authenticate

class OptionalPasswordChangeForm(auth.forms.PasswordChangeForm):
	"""
	Password change form that allows empty passwords.
	"""
	new_password1 = forms.CharField(required=False, label=_("New password"), widget=forms.PasswordInput)
	new_password2 = forms.CharField(required=False, label=_("New password confirmation"), widget=forms.PasswordInput)
	old_password = forms.CharField(required=False, label=_("Old password"), widget=forms.PasswordInput)

# single-user version of django.contrib.auth.forms.AuthenticationForm
class SingleUserLoginForm(auth.forms.AuthenticationForm):
	# make username field unrequired because we don't need it for authentication
	username = forms.CharField(label=_("User name"), required=False, max_length=30)
	# make password field unrequired because login with an empty shall be possible after installation
	password = forms.CharField(label=_("Password"), required=False, widget=forms.PasswordInput)

	def __init__(self, request, *args, **kwargs):
		request.session.set_test_cookie()
		super().__init__(request, *args, **kwargs)

	def clean(self):
		password = self.cleaned_data.get('password')

		self.user_cache = authenticate(password=password)
		if self.user_cache is None:
			raise forms.ValidationError(_("Please enter the correct password, case-sensitive."))

		# TODO: check whether this has moved to its own method in later Django versions (currently 1.2 pre).
		if self.request:
			if not self.request.session.test_cookie_worked():
				raise forms.ValidationError(_("Your Web browser doesn't appear to have cookies enabled. Cookies are required for logging in."))

		return self.cleaned_data
