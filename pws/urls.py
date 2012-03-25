from django.conf.urls import *
from django.conf import settings
from django.views.generic import ListView
from u51.pws.models import Entry
from u51.pws import views, forms

urlpatterns = patterns('',
	(r'^$', views.main, {}, 'main'),
	(r'^edit/$', views.update_entry, {}, 'update'),
	(r'^edit/(?P<id>\d+)/$', views.update_entry, {}, 'edit'),
	(r'^delete/$', views.delete_entry, {}, 'delete'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^test/pwlist/$', ListView.as_view(model=Entry, template_name='test-pwlist'), {}, 'test-pwlist'),
		#(r'^test/pwlist/$', list_detail.object_list, {'queryset': Entry.objects.all(), 'template_object_name': 'entry'}, 'test-pwlist'),

		(r'^test/edit/$', views.update_entry, {'next': 'test-update', 'template': 'pws/pwform.html'}, 'test-update'),
		(r'^test/edit/(?P<id>\d+)/$', views.update_entry, {'next': 'test-update', 'template': 'pws/pwform.html'}, 'test-edit'),

		(r'^test/edit/flat/$', views.update_entry, {'next': 'test-update-flat', 'template': 'pws/pwform-flat.html'}, 'test-update-flat'),
		(r'^test/edit/(?P<id>\d+)/flat/$', views.update_entry, {'next': 'test-update-flat', 'template': 'pws/pwform-flat.html'}, 'test-edit-flat'),
	)

