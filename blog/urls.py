#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from blog import views


urlpatterns = patterns('',
                       url(r'^$', views.post_list, name='post_list'),
                       url(r'^new/$', views.post_new, name='post_new'),
                       url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
                       url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
                       url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
                       url(r'^(?P<pk>\d+)/like/$', views.post_like, name='post_like'),
                       url(r'^(?P<pk>\d+)/add/$', views.add_comment, name='add_comment'),
                       url(r'^(?P<pk>\d+)/views/$', views.post_views, name='post_views'),



                       )
