from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import list_detail
from django.views.i18n import javascript_catalog
from django.contrib.auth.views import login, logout_then_login, password_change, password_change_done
from tools.forms import SingleUserLoginForm, OptionalPasswordChangeForm

# admin.autodiscover()

urlpatterns = patterns('',
	(r'^', include('u51.pws.urls')),

	(r'^jsi18n/(?P<packages>\S+?)$', javascript_catalog),

	(r'^login/$', login, {'template_name': 'login.html', 'authentication_form': SingleUserLoginForm}, 'login'),
	(r'^logout/$', logout_then_login, {}, 'logout'),
	(r'^settings/$', password_change, {'template_name': 'settings/password_change_form.html', 'password_change_form': OptionalPasswordChangeForm, 'post_change_redirect': '/settings/password_change_done/'}, 'settings'),
	(r'^settings/password_change_done/$', password_change_done, {'template_name': 'settings/password_change_done.html'}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
