#-*- coding: utf-8 -*-
from django.conf.urls import url
from interior.views import interior_views

urlpatterns = [
   
    url(r'^$', interior_views, name='interior'),
   
    
]