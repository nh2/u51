from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic import list_detail
from django.contrib.auth.views import login, logout_then_login, password_change, password_change_done
from u51.pws import forms

# admin.autodiscover()

urlpatterns = patterns('',
	(r'^', include('u51.pws.urls')),

	(r'^login/$', login, {'template_name': 'pws/login.html', 'authentication_form': forms.LoginForm}, 'login'),
	(r'^logout/$', logout_then_login, {}, 'logout'),
	(r'^settings/$', password_change, {'template_name': 'settings/password_change_form.html', 'password_change_form': forms.OptionalPasswordChangeForm, 'post_change_redirect': '/settings/password_change_done/'}, 'settings'),
	(r'^settings/password_change_done/$', password_change_done, {'template_name': 'settings/password_change_done.html'}),
)

if settings.DEBUG:
	from django.views.static import serve
	import os
	urlpatterns += patterns('',
		(r'^media/(.*)$', serve, {'document_root': os.path.join(settings.PROJECT_ROOT, '..', 'media')}),
	)
