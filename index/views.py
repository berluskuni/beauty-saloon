#-*- coding: utf-8 -*-
from django.contrib import auth
from django.shortcuts import render_to_response
from index.models import AboutMe
from django.contrib.auth.models import User


def index(request):
    username = auth.get_user(request).username
    if request.user.is_authenticated():
        user = User.objects.get(username=username)
        per = user.has_module_perms('clients')
        return render_to_response('index.html', {'about_me': AboutMe.objects.all(), 'username': username, 'per': per })
    
    return render_to_response('index.html', {'about_me': AboutMe.objects.all(), 'username': username })

