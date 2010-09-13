from django import template

register = template.Library()

from u51.pws.models import Eintrag
from u51.pws.forms import EintragForm
from django.core.urlresolvers import reverse

@register.inclusion_tag('pws/pwlist.html')
def include_pwlist():
	return {
		'eintrag_list': Eintrag.objects.all(),
	}

@register.inclusion_tag('pws/pwform-flat.html', takes_context=True)
def include_pwform(context):
	pwform = context.get('pwform') or EintragForm()
	edit = True if pwform.instance.id else False
	action = reverse('edit', args=[pwform.instance.id]) if edit else reverse('update')
	return {
		'pwform': pwform,
		'edit': edit,
		'action': action,
	}

@register.inclusion_tag('pws/ausfuellfehler.html')
def ausfuellfehler(messagewrap):
	return {
		'message': messagewrap,
	}

@register.inclusion_tag('pws/ausfuellfehler_message.html')
def ausfuellfehler_message(message):
	return {
		'message': message,
	}

@register.inclusion_tag('pws/loeschform.html')
def loeschform(value, text="X", action=""):
	return {
		'value': value,
		'text': text,
		'action': action,
	}
