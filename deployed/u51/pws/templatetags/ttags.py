from django import template

register = template.Library()

from u51.pws.models import Eintrag

@register.inclusion_tag('pws/liste.html')
def include_liste():
	return {
		'eintrag_list': Eintrag.objects.all(),
	}

@register.inclusion_tag('pws/form-flat.html', takes_context=True)
def include_form(context):
	return {
		'form': context['form'],
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
