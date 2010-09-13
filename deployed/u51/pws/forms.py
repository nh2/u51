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
		self.fields['pw'].widget = forms.PasswordInput(render_value=True, attrs={'autocomplete': 'off'})

	submit_name = 'create_edit_eintrag'


from django.contrib.auth.forms import AuthenticationForm

# single-user version of django.contrib.auth.forms.AuthenticationForm
class LoginForm(AuthenticationForm):
	# make username field unrequired because we don't need it for authentication
	username = forms.CharField(label=_("Username"), required=False, max_length=30)
	# make password field unrequired because login with an empty shall be possible after installation
	password = forms.CharField(label=_("Password"), required=False, widget=forms.PasswordInput)

	def clean(self):
		password = self.cleaned_data.get('password')

		from django.contrib.auth import authenticate
		self.user_cache = authenticate(password=password)
		if self.user_cache is None:
			raise forms.ValidationError(_("Please enter the correct password, case-sensitive."))

		# TODO: check whether this has moved to its own method in later Django versions (currently 1.2 pre).
		if self.request:
			if not self.request.session.test_cookie_worked():
				raise forms.ValidationError(_("Your Web browser doesn't appear to have cookies enabled. Cookies are required for logging in."))

		return self.cleaned_data
