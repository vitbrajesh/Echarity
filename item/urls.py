from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.p_list, name='p_list'),
    url(r'^list/(?P<pk>[0-9]+)/$', views.p_detail, name='p_detail'),
]

