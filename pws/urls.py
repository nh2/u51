from django.conf import settings
from django.conf.urls import *
from django.urls import include, path
from django.views.generic import ListView
from pws.models import Entry
from pws import views, forms

urlpatterns = [
	path('', views.main, {}, 'main'),
	path('edit/', views.update_entry, {}, 'update'),
	path('edit/<int:id>/', views.update_entry, {}, 'edit'),
	path('delete/', views.delete_entry, {}, 'delete'),
]

if settings.DEBUG:
	urlpatterns += [
		path('test/pwlist/', ListView.as_view(model=Entry, template_name='test-pwlist'), {}, 'test-pwlist'),
		#path('test/pwlist/', list_detail.object_list, {'queryset': Entry.objects.all(), 'template_object_name': 'entry'}, 'test-pwlist'),

		path('test/edit/', views.update_entry, {'next': 'test-update', 'template': 'pws/pwform.html'}, 'test-update'),
		path('test/edit/<int:id>/', views.update_entry, {'next': 'test-update', 'template': 'pws/pwform.html'}, 'test-edit'),

		path('test/edit/flat/', views.update_entry, {'next': 'test-update-flat', 'template': 'pws/pwform-flat.html'}, 'test-update-flat'),
		path('test/edit/<int:id>/flat/', views.update_entry, {'next': 'test-update-flat', 'template': 'pws/pwform-flat.html'}, 'test-edit-flat'),
	]

