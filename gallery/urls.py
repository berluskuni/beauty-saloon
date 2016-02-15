#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from gallery.models import Album, Photo
from gallery import views
#
urlpatterns = patterns('',
    
    url(r'^$', views.album_list, name='album_list'),
    url(r'^(?P<slug>[\w-]+)/$', views.album_detail, name='photos'),
    url(r'^(?P<slug>[\w-]+)/photo_load/$', views.photo_load, name='photo_load'),
    url(r'^(?P<slug>[\w-]+)(?P<pk>\d+)/photo_delete/$', views.photo_delete, name='photo_delete'),
    url(r'^(?P<slug>[\w-]+)/(?P<pk>\d+)/$', views.album_paginator, name='paginator'),
)