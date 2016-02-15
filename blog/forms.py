#-*- coding: utf-8 -*-

from django import forms
from blog.models import Post, Comments
# from ckeditor.widgets import CKEditorWidget


class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'text_redactor']


class PostDelete(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title']


class PostComments(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']