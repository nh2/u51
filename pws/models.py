from django.db import models
from django.utils.translation import gettext_lazy as _

class Entry(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(_('Where'), max_length=200, unique=True)
	user = models.CharField(_('User'), max_length=200, blank=True)
	pw = models.CharField(_('Password'), max_length=200, blank=True)
	email = models.EmailField(_('Email'), blank=True)
	extra = models.TextField(_('Extra info'), blank=True)
	created = models.DateField(_('Created'), auto_now=True)
	modified = models.DateField(_('Changed'), auto_now_add=True)

	class Meta:
		ordering = ['name']
		verbose_name = _('Entry')
		verbose_name_plural = _('Entries')
