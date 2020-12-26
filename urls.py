from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog
from django.contrib.auth.views import LoginView, logout_then_login, PasswordChangeView, PasswordChangeDoneView
from tools.forms import SingleUserLoginForm, OptionalPasswordChangeForm

# admin.autodiscover()

urlpatterns = [
	path('', include('u51.pws.urls')),

	path('jsi18n/',
		JavaScriptCatalog.as_view(),
		name='javascript-catalog',
	),

	path('login/',
		LoginView.as_view(
			template_name='login.html',
			authentication_form=SingleUserLoginForm,
		),
		name='login',
	),
	path('logout/', logout_then_login, {}, 'logout'),
	path('settings/',
		PasswordChangeView.as_view(
			template_name='settings/password_change_form.html',
			form_class=OptionalPasswordChangeForm,
			success_url='/settings/password_change_done/',
		),
		name='settings',
	),
	path('settings/password_change_done/',
		PasswordChangeDoneView.as_view(
			template_name='settings/password_change_done.html',
		),
	),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
