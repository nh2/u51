from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from u51.pws import models

class EintragForm(forms.ModelForm):

	class Meta:
		model = models.Eintrag
		fields = ['name', 'user', 'pw', 'email', 'extra']

	def __init__(self, *args, **kwargs):
		super(EintragForm, self).__init__(*args, **kwargs)
		self.fields['extra'].widget.attrs = {'cols': 24, 'rows': 5}
		self.fields['pw'].widget = forms.PasswordInput(render_value=True)

	submit_name = 'create_edit_eintrag'


# single-user version of django.contrib.auth.forms.AuthenticationForm
class LoginForm(forms.Form):

	password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

	def __init__(self, request=None, *args, **kwargs):
		"""
		If request is passed in, the form will validate that cookies are
		enabled. Note that the request (a HttpRequest object) must have set a
		cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
		running this validation.
		"""
		self.request = request
		self.user_cache = None
		super(LoginForm, self).__init__(*args, **kwargs)

	def clean(self):
		password = self.cleaned_data.get('password')

		if password:
			from django.contrib.auth import authenticate
			self.user_cache = authenticate(password=password)
			if self.user_cache is None:
				raise forms.ValidationError(_("Please enter the correct password, case-sensitive."))

		# TODO: check whether this has moved to its own method in later Django versions (currently 1.1).
		if self.request:
			if not self.request.session.test_cookie_worked():
				raise forms.ValidationError(_("Your Web browser doesn't appear to have cookies enabled. Cookies are required for logging in."))

		return self.cleaned_data

	def get_user_id(self):
		if self.user_cache:
			return self.user_cache.id
		return None

	def get_user(self):
		return self.user_cache

