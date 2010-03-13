from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse
from u51.pws.models import Eintrag, EintragForm

def create_edit_eintrag(request, id=None, flat=False):
	form = EintragForm(request.POST or None, instance=(id and Eintrag.objects.get(id=id)), label_suffix='')

	if request.method == 'POST' and form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('liste'))

	if flat:
		template = 'pws/create_edit_eintrag-flat.html'
	else:
		template = 'pws/create_edit_eintrag.html'

	return direct_to_template(request, template, {'form': form})
