from django.db import models

class Eintrag(models.Model):
	name = models.CharField(max_length=200)
	user = models.CharField(max_length=200)
	pw = models.CharField('Passwort', max_length=200)
	email = models.EmailField()
	extra = models.TextField(blank=True)
	eingetragen = models.DateField(auto_now=True)
	geaendert = models.DateField(auto_now_add=True)

from django import forms
from django.forms import ModelForm
from django.forms.widgets import Textarea

class EintragForm(ModelForm):
	class Meta:
		model = Eintrag
	pw = forms.CharField(widget=forms.PasswordInput(render_value=True))
	extra = forms.CharField(widget=forms.Textarea(attrs={'cols': 24, 'rows': 5}))
	fields = ('name', 'user', 'pw', 'email', 'extra')
