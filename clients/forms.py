#-*- coding: utf-8 -*-
__author__ = 'berluskuni'

from django import forms
from clients.models import Clients, Search


class ClientsForms(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'number', 'formula']


class ClientsDelete(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['number']
        
class ClientsSearch(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['number']

