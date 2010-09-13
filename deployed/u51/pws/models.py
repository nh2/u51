from django.db import models

class Eintrag(models.Model):
	name = models.CharField(max_length=200,unique=True)
	user = models.CharField(max_length=200)
	pw = models.CharField('Passwort', max_length=200)
	email = models.EmailField()
	extra = models.TextField(blank=True)
	eingetragen = models.DateField(auto_now=True)
	geaendert = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ['name']
