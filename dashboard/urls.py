from django.conf.urls import patterns, include, url

urlpatterns = patterns('dashboard.views',
    
    url(r'^edit/$', 'edit', name='edit'),
    url(r'^profile/(?P<pk>[0-9]+)/edit/$', 'profile_edit', name='profile_edit'),

)
