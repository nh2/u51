from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from u51.pws.models import Eintrag
from u51.pws.forms import EintragForm
from u51.tools.json import json_response

@login_required
def update_eintrag_get_pwform(request, id=None):
	submitted = (request.method == 'POST') and request.POST
	form = EintragForm(submitted or None, instance=(id and get_object_or_404(Eintrag, id=id)), label_suffix='')

	if submitted and form.is_valid():
		form.save()

	return form

@login_required
def main(request, template='pws/main.html'):
	return direct_to_template(request, template)

@login_required
def update_eintrag(request, id=None, template='pws/main.html', next='main'):
	form = update_eintrag_get_pwform(request, id)
	if form.is_valid():
		return redirect(next)
	return direct_to_template(request, template, {'pwform': form})

@login_required
def delete_eintrag(request, next='main'):
	submitted = (request.method == 'POST') and request.POST
	if submitted:
		json = {'success': False}
		try:
			eintrag = Eintrag.objects.get(id=submitted['loesch_id'])
			eintrag.delete()
			json['success'] = True
		except Eintrag.DoesNotExist:
			pass
		if request.is_ajax():
			return json_response(json)
	return redirect(next)
