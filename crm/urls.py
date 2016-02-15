from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.client_list, name='client_list'),
    
    url(r'^(?P<pk>[0-9]+)/$', views.client_list, name='client_list'),
    
    url(r'^client/(?P<pk>[0-9]+)$',
		views.client_details, name='client_details'),
        
    url(r'^client/(?P<pk>[0-9]+)/edit$',
		views.client_edit, name='client_edit'),
        
	url(r'^logout/$', 'django.contrib.auth.views.logout',
                      {'next_page': '/'}),
                      
    url(r'^login/$', views.login_view, name='login_view'),
]
