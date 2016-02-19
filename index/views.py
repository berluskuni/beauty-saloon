#-*- coding: utf-8 -*-
from django.contrib import auth
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from index.models import AboutMe
from django.contrib.auth.models import User


def index(request):
    args = {}
    args.update(csrf(request))
    args['about_me'] = AboutMe.objects.all()
    args['username'] = auth.get_user(request).username
    if request.user.is_authenticated():
        user = User.objects.get(username=args['username'])
        per = user.has_module_perms('clients')
        args['per'] = user.has_module_perms('clients')
        return render_to_response('index.html', args)
    
    return render_to_response('index.html', args)

