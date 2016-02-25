#-*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


def login_in(request):
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)
    else:
        return HttpResponse(status=405)


def logout_out(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = authenticate(username=newuser_form.cleaned_data['username'],
                                   password=newuser_form.cleaned_data['password1'])
            login(request, newuser)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)
    return HttpResponse(status=405)
