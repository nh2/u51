from django.db import models
from django.forms import ModelForm

class Eintrag(models.Model):
	name = models.CharField(max_length=200)
	user = models.CharField(max_length=200)
	pw = models.CharField('Passwort', max_length=200)
	email = models.EmailField()
	extra = models.TextField(blank=True)
	eingetragen = models.DateField(auto_now=True)
	geaendert = models.DateField(auto_now_add=True)

class EintragForm(ModelForm):
	class Meta:
		model = Eintrag
		fields = ('name', 'user', 'pw', 'email', 'extra')
