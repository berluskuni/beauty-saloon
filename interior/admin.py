#-*- coding: utf-8 -*-
from django.contrib import admin
from interior.models import Photo, PhotoTh

class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ['title', 'img', 'img_litle', 'index', 'alt']})
    ]
    list_display = ['title', 'index', 'alt', 'img', 'img_litle']
    ordering = ['title']
    
class PhotoThAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ['title', 'img_th', 'index', 'alt']})
    ]
    list_display = ['title', 'index', 'alt', 'img_th']
    ordering = ['title']

# Register your models here.

admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoTh, PhotoThAdmin)
