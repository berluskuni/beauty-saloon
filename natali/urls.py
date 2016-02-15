#-*- coding: utf-8 -*-
"""natali URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^$', include('index.urls', namespace='index')),
    url(r'^interior/', include('interior.urls', namespace='salon')),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^auth/', include('loginsys.urls', namespace='login')),
    url(r'^post/', include('blog.urls', namespace='post')),
    url(r'^clients/', include('clients.urls', namespace='clients')),
    url(r'^contacts/', include('contacts.urls', namespace='contacts')),
]

# ckeditor
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += patterns('',
                        (r'^ckeditor/', include('ckeditor.urls'))
       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
       
# end ckeditor
