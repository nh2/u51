from django import template
from templatetag_sugar.register import tag
from templatetag_sugar.parser import *

register = template.Library()

from pws.models import Entry
from pws.forms import EntryForm
from django.urls import reverse
from django.db.models import Q

@tag(register, [Variable(), Constant("as"), Name()])
def empty_password(context, user, asvar):
	context[asvar] = user.check_password('')
	return ""

@register.inclusion_tag('pws/pwlist.html', takes_context=True)
def include_pwlist(context):
	f = context.get('entry_filter')
	entries = Entry.objects.filter(Q(name__contains=f) | Q(user__contains=f) | Q(email__contains=f) | Q(extra__contains=f)) if f else Entry.objects.all()
	return {
		'entry_list': entries,
		'entry_filter': f,
		'plain': context.get('plain'),
	}

@register.inclusion_tag('pws/pwform-flat.html', takes_context=True)
def include_pwform(context):
	return {
		'pwform': context.get('pwform', EntryForm()),
		'edit': context.get('edit', False),
		'action': context.get('action', reverse('update')),
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
def deleteform(delete_id, delete_text="X", action=reverse('delete')):
	return {
		'delete_id': delete_id,
		'delete_text': delete_text,
		'action': action,
	}

