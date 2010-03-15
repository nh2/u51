from django import forms
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
