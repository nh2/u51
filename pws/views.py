from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from pws.models import Entry
from pws.forms import EntryForm
from u51.tools.json import json_response

@login_required
def update_entry_get_pwform(request, id=None):
	submitted = (request.method == 'POST') and request.POST
	form = EntryForm(submitted or None, instance=(id and get_object_or_404(Entry, id=id)), label_suffix='')

	if submitted and form.is_valid():
		form.save()

	return form

@login_required
def main(request, template='pws/main.html'):
	entry_filter = request.method == 'GET' and request.GET.get('filter')
	plain = request.method == 'GET' and 'plain' in request.GET
	return render(request, template, {'entry_filter': entry_filter, 'plain': plain})

@login_required
def update_entry(request, id=None, template='pws/main.html', next='main'):
	pwform = update_entry_get_pwform(request, id)
	edit = True if pwform.instance.id else False
	action = reverse('edit', args=[pwform.instance.id]) if edit else reverse('update')
	if pwform.is_valid():
		return redirect(next)
	return render(request, template, {'pwform': pwform, 'edit': edit, 'action': action})

@login_required
def delete_entry(request, next='main'):
	submitted = (request.method == 'POST') and request.POST
	if submitted:
		json = {'success': False}
		try:
			entry = Entry.objects.get(id=submitted['delete_id'])
			entry.delete()
			json['success'] = True
		except Entry.DoesNotExist:
			pass
		if request.is_ajax():
			return json_response(json)
	return redirect(next)
