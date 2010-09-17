from django import forms
from django.utils.translation import ugettext_lazy as _
from u51.pws import models

class EntryForm(forms.ModelForm):

	class Meta:
		model = models.Entry
		fields = ['name', 'user', 'pw', 'email', 'extra']

	def __init__(self, *args, **kwargs):
		super(EntryForm, self).__init__(*args, **kwargs)
		self.fields['extra'].widget.attrs = {'cols': 24, 'rows': 5}
		self.fields['pw'].widget = forms.PasswordInput(render_value=True, attrs={'autocomplete': 'off'})

	submit_name = 'update_entry'
