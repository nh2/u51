import os
from django.conf.urls.defaults import *
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import list_detail
from django.contrib.auth.views import login, logout_then_login, password_change
from u51.pws.models import Eintrag
from u51.pws import views, forms

# admin.autodiscover()

eintraege = {
	'queryset': Eintrag.objects.all(),
	'template_object_name': 'eintrag',
}

urlpatterns = patterns('',
	(r'^$', views.main, {}, 'main'),
	(r'^edit/$', views.update_eintrag, {}, 'update'),
	(r'^edit/(?P<id>\d+)/$', views.update_eintrag, {}, 'edit'),
	(r'^delete/$', views.delete_eintrag),

	(r'^test/liste/$', list_detail.object_list, eintraege, 'liste'),
	
	(r'^test/edit/$', views.update_eintrag, {'next': 'test-edit', 'template': 'pws/pwform.html'}, 'test-update'),
	(r'^test/edit/(?P<id>\d+)/$', views.update_eintrag, {'next': 'test-edit', 'template': 'pws/pwform.html'}, 'test-edit'),
	
	(r'^test/edit/flat/$', views.update_eintrag, {'next': 'test-edit-flat', 'template': 'pws/pwform-flat.html'}, 'test-update-flat'),
	(r'^test/edit/(?P<id>\d+)/flat/$', views.update_eintrag, {'next': 'test-edit-flat', 'template': 'pws/pwform-flat.html'}, 'test-edit-flat'),

	(r'^login/$', login, {'template_name': 'pws/login.html', 'authentication_form': forms.LoginForm}, 'login'),
	(r'^logout/$', logout_then_login, {}, 'logout'),
	(r'^settings/$', password_change, {}, 'settings'),
)

if settings.DEBUG:
	from django.views.static import serve
	urlpatterns += patterns('',
		(r'^media/(.*)$', serve, {'document_root': os.path.join(settings.PROJECT_PATH, '..', 'media')}),
	)
