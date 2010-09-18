from django import forms
from u51.pws import models

class EntryForm(forms.ModelForm):

	class Meta:
		model = models.Entry
		fields = ['name', 'user', 'pw', 'email', 'extra']

	def __init__(self, *args, **kwargs):
		super(EntryForm, self).__init__(*args, **kwargs)
		self.fields['extra'].widget.attrs = {'cols': 20, 'rows': 5}
		self.fields['pw'].widget = forms.PasswordInput(render_value=True, attrs={'autocomplete': 'off'})

	submit_name = 'update_entry'
