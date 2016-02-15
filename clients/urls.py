#-*- coding: utf-8 -*-
from django.conf.urls import url
from clients import views

urlpatterns = [
    url(r'^$', views.clients_list, name='clients_list'),
    url(r'^(?P<pk>\d+)/$', views.clients_detail, name='clients_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.clients_edit, name='clients_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.clients_delete, name='clients_delete'),
    url(r'^clients_add/$', views.clients_add, name='clients_add'),
    url(r'^search/$', views.clients_search, name='clients_search'),
]