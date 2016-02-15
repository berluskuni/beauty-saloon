#-*- coding: utf-8 -*-
from django.contrib import admin
from clients.models import Clients, Search

# Register your models here.
class ClientsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ['name', 'number', 'formula']})
    ]
    list_display = ['name', 'number', 'formula']
    ordering = ['number']
    
    
    
admin.site.register(Clients, ClientsAdmin)
admin.site.register(Search)