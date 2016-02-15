#-*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth.models import User
from gallery.forms import PhotoForm, PhotoDelete
from gallery.models import Photo, Album
from django.contrib import auth
from django.core.paginator import Paginator



def photo_load(request, slug):
    photos = get_object_or_404(Album, slug=slug)
    username = auth.get_user(request).username
    if request.user.is_authenticated():
        user = User.objects.get(username=username)
        if user.has_module_perms('gallery'):
            if request.method == 'POST':
                form = PhotoForm(request.POST,  request.FILES or None)
                if form.is_valid():
                    obj = Album(img=request.FILES['img'])
                    obj = form.save(commit=False)
                    obj.save()
                    return render(request, 'photo_album.html', {'photos': photos, 'username': auth.get_user(request).username})
            else:
                form = PhotoForm
                return render(request, 'photo_load.html', {'form': form, 'username': auth.get_user(request).username})
        else:
            return render(request, 'photo_add.html')
    else:
        return render(request, 'photo_add.html')
    return render(request, 'photo_album.html', {'photos': photos, 'username': auth.get_user(request).username})
"""  
def photo_delete(request, slug):
    photos = get_object_or_404(Album, slug=slug)
    username = auth.get_user(request).username
    if request.user.is_authenticated():
        user = User.objects.get(username=username)
        if user.has_module_perms('gallery'):
            if request.method == 'POST':
                form = PhotoDelete(request.POST)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    photo = Photo.objects.get(title=title)
                    photo.delete()
                    return render(request, 'photo_album.html', {'photos': photos, 'username': auth.get_user(request).username})
            else:
                form = PhotoDelete
                return render(request, 'photo_delete.html', {'photos': photos, 'form': form, 'username': auth.get_user(request).username})
        else:
            return render(request, 'photo_add.html')
    else:
        return render(request, 'photo_add.html')
    return render(request, 'photo_album.html', {'photos': photos, 'username': auth.get_user(request).username})
"""              
def photo_delete(request, slug, pk):
    args = {}
    args['page_number'] = pk
    args['slug'] = slug
    photos = get_object_or_404(Album, slug=slug).photo_set.all()
    current_page = Paginator(photos, 3)
    args['photos'] = current_page.page(pk)
    args['username'] = auth.get_user(request).username
    username = auth.get_user(request).username
    if request.user.is_authenticated():
        user = User.objects.get(username=username)
        if user.has_module_perms('gallery'):
            if request.method == 'POST':
                form = PhotoDelete(request.POST)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    photo = Photo.objects.get(title=title)
                    photo.delete()
                    return render(request, 'photo_album.html', args)
            else:
                args['form'] = PhotoDelete
                return render(request, 'photo_delete.html', args)
        else:
            return render(request, 'photo_add.html')
    else:
        return render(request, 'photo_add.html')
    return render(request, 'photo_album.html', args)                    
    
        
"""       
def album_detail(request, slug):
    photos = get_object_or_404(Album, slug=slug)
    return render(request, 'photo_album.html', {'photos':photos, 'username': auth.get_user(request).username})
"""

def album_detail(request, slug, page_number=1):
    args = {}
    args['page_number'] = page_number
    args['slug'] = slug
    photos = get_object_or_404(Album, slug=slug).photo_set.all()
    current_page = Paginator(photos, 3)
    args['photos'] = current_page.page(page_number)
    args['username'] = auth.get_user(request).username
    
    return render(request, 'photo_album.html', args)
    
    
def album_paginator(request, slug, pk):
    args = {}
    args['page_number'] = pk
    args['slug'] = slug
    photos = get_object_or_404(Album, slug=slug).photo_set.all()
    current_page = Paginator(photos, 3)
    args['photos'] = current_page.page(pk)
    args['username'] = auth.get_user(request).username
    
    return render(request, 'photo_album.html', args)


def album_list(request):
    my_album = Album.objects.all()
    return render(request, 'album.html', {'my_album': my_album, 'username': auth.get_user(request).username})
                
