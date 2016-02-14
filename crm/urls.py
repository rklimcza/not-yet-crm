from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.client_list, name='client_list'),
    url(r'client_list/^$', views.client_list, name='client_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.client_list, name='client_list'),
]
