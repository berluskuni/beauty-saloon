#-*- coding: utf-8 -*-
from django.contrib import auth
from django.shortcuts import render_to_response
from interior.models import Photo

# Create your views here.
def interior_views(request):
    args = {}
    args['header'] = 'Интерьер салона'
    args['vhod'] = Photo.objects.get(index=0)
    args['parikzal'] = Photo.objects.get(index=1)
    args['vnutri'] = Photo.objects.get(index=2)
    args['moyka'] = Photo.objects.get(index=3)
    args['manikur'] = Photo.objects.get(index=4)
    args['man_dr_vid'] = Photo.objects.get(index=5)
    args['massag'] = Photo.objects.get(index=6)
    args['username'] = str(auth.get_user(request).username)
    return render_to_response('interior.html', args)
                               


