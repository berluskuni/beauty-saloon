#-*- coding: utf-8 -*-
from django import forms
from gallery.models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'album', 'img']
        
class PhotoDelete(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title']