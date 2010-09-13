from django import template

register = template.Library()

from u51.pws.models import Entry
from u51.pws.forms import EntryForm
from django.core.urlresolvers import reverse

@register.inclusion_tag('pws/pwlist.html')
def include_pwlist():
	return {
		'entry_list': Entry.objects.all(),
	}

@register.inclusion_tag('pws/pwform-flat.html', takes_context=True)
def include_pwform(context):
	pwform = context.get('pwform') or EntryForm()
	edit = True if pwform.instance.id else False
	action = reverse('edit', args=[pwform.instance.id]) if edit else reverse('update')
	return {
		'pwform': pwform,
		'edit': edit,
		'action': action,
	}

@register.inclusion_tag('pws/inputerror.html')
def inputerror(messagewrap):
	return {
		'message': messagewrap,
	}

@register.inclusion_tag('pws/inputerror_message.html')
def inputerror_message(message):
	return {
		'message': message,
	}

@register.inclusion_tag('pws/deleteform.html')
def deleteform(value, text="X", action=""):
	return {
		'value': value,
		'text': text,
		'action': action,
	}
