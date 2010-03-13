import os
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic import list_detail
from u51.pws.models import Eintrag
from u51.pws import views

# admin.autodiscover()

eintraege = {
	'queryset': Eintrag.objects.all(),
	'template_object_name': 'eintrag',
}

urlpatterns = patterns('',
	(r'^$', list_detail.object_list, eintraege, 'liste'),
	(r'^edit/$', views.create_edit_eintrag),
	(r'^edit/(?P<id>\d+)/$', views.create_edit_eintrag),
	(r'^edit/flat/$', views.create_edit_eintrag, {'flat': True}),
	(r'^edit/(?P<id>\d+)/flat$', views.create_edit_eintrag, {'flat': True}),
)

if settings.DEBUG:
	from django.views.static import serve
	urlpatterns += patterns('',
		(r'^media/(.*)$', serve, {'document_root': os.path.join(settings.PROJECT_PATH, '..', 'media')}),
	)
