import os
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic import list_detail
from django.contrib.auth.views import login, logout_then_login
from u51.pws.models import Eintrag
from u51.pws import views, forms

# admin.autodiscover()

eintraege = {
	'queryset': Eintrag.objects.all(),
	'template_object_name': 'eintrag',
}
eintraege_main = {
	'template_name': 'pws/main.html'
}
eintraege_main.update(eintraege)

urlpatterns = patterns('',
	(r'^$', views.main, {}, 'main'),
	(r'^edit/$', views.main_update_eintrag, {}, 'update'),
	(r'^edit/(?P<id>\d+)/$', views.main_update_eintrag, {}, 'edit'),
	(r'^delete/$', views.main_delete_eintrag, {}),

	(r'^test/liste/$', list_detail.object_list, eintraege, 'liste'),
	(r'^test/edit/$', views.eintrag_editor),
	(r'^test/edit/(?P<id>\d+)/$', views.eintrag_editor),
	(r'^test/edit/flat/$', views.eintrag_editor, {'flat': True}),
	(r'^test/edit/(?P<id>\d+)/flat$', views.eintrag_editor, {'flat': True}),

	(r'^login/$', login, {'template_name': 'pws/login.html', 'authentication_form': forms.LoginForm}, 'login'),
	(r'^logout/$', logout_then_login, {}, 'logout'),
)

if settings.DEBUG:
	from django.views.static import serve
	urlpatterns += patterns('',
		(r'^media/(.*)$', serve, {'document_root': os.path.join(settings.PROJECT_PATH, '..', 'media')}),
	)
