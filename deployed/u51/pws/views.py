from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.simple import direct_to_template
from django.utils import simplejson
from u51.pws.models import Eintrag
from u51.pws.forms import EintragForm

def update_eintrag(request, id=None):
	submitted = (request.method == 'POST') and request.POST
	form = EintragForm(submitted or None, instance=(id and get_object_or_404(Eintrag, id=id)), label_suffix='')

	if submitted and form.is_valid():
		form.save()

	return form

def eintrag_editor(request, id=None, flat=False):
	form = create_edit_eintrag(request, id)
	if form.is_valid():
		return redirect('liste')

	if flat:
		template = 'pws/update_eintrag-flat.html'
	else:
		template = 'pws/update_eintrag.html'

	return direct_to_template(request, template, {'form': form})

def main(request, form=None):
	form = form or update_eintrag(request, None)
	return direct_to_template(request, 'pws/main.html', {'form': form})

def main_update_eintrag(request, id=None):
	form = update_eintrag(request, id)
	if form.is_valid():
		return redirect('main')
	# ID explizit setzen, macht ModelForm nicht selbst
	form.id = id
	return main(request, form=form)

def main_delete_eintrag(request):
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
	return redirect('main')

def json_response(json):
	return HttpResponse(simplejson.dumps(json), mimetype='application/javascript')
