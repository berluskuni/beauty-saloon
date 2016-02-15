#-*- coding: utf-8 -*-
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from blog.models import Post, Comments
from blog.forms import PostForms, PostDelete, PostComments
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


def post_list(request):
    """
    Вывод всех постов!
    """
    username = auth.get_user(request).username
    if request.user.is_authenticated():
        user = User.objects.get(username=username)
        per = user.has_module_perms('blog')
        return render_to_response('post_list.html', {'post_list': Post.objects.all(),
                                                 'username': auth.get_user(request).username, 'per': per})
    return render_to_response('post_list.html', {'post_list': Post.objects.all(),
                                                 'username': auth.get_user(request).username})


def post_new(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = PostForms(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post:post_detail', pk=post.pk)
        else:
            form = PostForms
            return render(request, 'post_edit.html', {'form': form, 'username': auth.get_user(request).username})
    else:
        return render_to_response('post_new.html')


def post_detail(request, pk):
    if request.user.is_authenticated():
        if auth.get_user(request).username == str(Post.objects.get(pk=pk).author):
            post = get_object_or_404(Post, pk=pk)
            return render(request, 'post_detail.html', {'post': post, 'username': auth.get_user(request).username})
        else:
            comments_form = PostComments
            args = {}
            args.update(csrf(request))
            args['post_views'] = Post.objects.get(pk=pk)
            args['comments'] = Comments.objects.filter(comments_post_id=pk)
            args['form'] = comments_form
            args['username'] = auth.get_user(request).username
            args['author'] = Post.objects.get(pk=pk).author
            return render_to_response('post_views.html', args)
    else:
        comments_form = PostComments
        args = {}
        args.update(csrf(request))
        args['post_views'] = Post.objects.get(pk=pk)
        args['comments'] = Comments.objects.filter(comments_post_id=pk)
        args['form'] = comments_form
        args['username'] = auth.get_user(request).username
        args['author'] = Post.objects.get(pk=pk).author
    return render_to_response('post_views.html', args)



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForms(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post:post_detail', pk=post.pk)
    else:
        form = PostForms(instance=post)

    return render(request, 'post_edit.html', {'form': form})

"""
def post_delete(request, pk):
    post_delete = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostDelete(request.POST, instance=post_delete)
        if form.is_valid():
            post = form.delete(commit=False)
            post.author = request.user
            post_delete.delete()
            return render_to_response('delete.html')
    else:
        form = PostDelete(instance=post_delete)
    return render(request, 'post_delete.html', {'form': form})
"""


def post_delete(request, pk):
    if request.user.is_authenticated():
        post_delete = get_object_or_404(Post, pk=pk)
        form = PostDelete(request.POST, instance=post_delete)
        if form.is_valid():
            post_delete.delete()
            return render_to_response('delete_post.html')
        else:
            form = PostDelete(instance=post_delete)
    else:
        post_views = get_object_or_404(Post, pk=pk)
        return render(request, 'post_views.html', {'post_views': post_views, 'username': auth.get_user(request).username})

    return render(request, 'post_delete.html', {'form': form})

"""
Использовать Cookies файлы для защиты серьезных действий не следует  т.к их легко можно
редактировать удалять и т.д
"""


def post_like(request, pk):
    try:
        if pk in request.COOKIES:
            redirect('/post/')
        else:
            post = Post.objects.get(pk=pk)
            post.post_like += 1
            post.save()
            response = redirect('/post/')
            response.set_cookie(pk, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/post/')


def post_views(request, pk):
    post_views = Post.objects.get(pk=pk)
    comments = Comments.objects.filter(comments_post_id=pk)
    return render_to_response('post_list_comment.html', {'post_views': post_views, 'comments': comments,
                                                         'username': auth.get_user(request).username})

"""
Использование сесий более надежно чем использование cookies
"""


def add_comment(request, pk):
    if request.POST and ('pause' not in request.session):
        form = PostComments(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_post = Post.objects.get(pk=pk)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/post/%s/' % pk)

