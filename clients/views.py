#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.contrib import auth
from django.http import Http404
from clients.models import Clients
from clients.forms import ClientsForms, ClientsDelete, ClientsSearch

# Create your views here.

def clients_add(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = ClientsForms(request.POST)
            if form.is_valid():
                clients = form.save(commit=False)
                clients.save()
                return redirect('clients:clients_detail', pk=clients.pk)
        else:
            form = ClientsForms
    return render(request, 'clients_edit.html', {'form': form, 'username': auth.get_user(request).username})
 

def clients_detail(request, pk):
    if request.user.is_authenticated():
        clients = get_object_or_404(Clients, pk=pk)
        return render(request, 'clients_detail.html', {'clients': clients, 'username': auth.get_user(request).username})
    return redirect('index:index')
        
        
def clients_edit(request, pk):
    clients = get_object_or_404(Clients, pk=pk)
    if request.method == 'POST':
        form = ClientsForms(request.POST, instance=clients)
        if form.is_valid():
            clients = form.save(commit=False)
            clients.save()
            return redirect('clients:clients_detail', pk=pk)
    else:
        form = ClientsForms(instance=clients)

    return render(request, 'clients_edit.html', {'form': form, 'username': auth.get_user(request).username})
    
    
def clients_list(request):
    """
    Вывод всех клиентов!
    """
    return render_to_response('clients_list.html', {'clients_list': Clients.objects.all(),
                                                 'username': auth.get_user(request).username})
                                                 
                                                 
def clients_delete(request, pk):
    if request.user.is_authenticated():
        clients_delete = get_object_or_404(Clients, pk=pk)
        form = ClientsDelete(request.POST, instance=clients_delete)
        if form.is_valid():
            clients_delete.delete()
            return render_to_response('delete.html', {'username': auth.get_user(request).username} )
        else:
            form = ClientstDelete(instance=clients_delete)
    else:
        return redirect('index:index')

    return render(request, 'clients_delete.html', {'form': form, 'username': auth.get_user(request).username})
    
    
def clients_search(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = ClientsSearch(request.POST)
            if form.is_valid():
                number = form.cleaned_data['number']
                clients = Clients.objects.get(number=number)
                return render_to_response('clients_detail.html',{'clients': clients, 'username': auth.get_user(request).username})
        else:
            form = ClientsSearch
    return render(request, 'clients_search.html', {'form': form, 'username': auth.get_user(request).username})
    