#-*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField # импорт ckeditor

# Create your models here.

# запоминать пользователя
# автосохранение


class Post(models.Model):
    class Meta:
        db_table = 'db_blog_app'

    author = models.ForeignKey('auth.User')
    post_title = models.CharField(max_length=200, verbose_name='Название статьи')
    text_redactor = RichTextField(blank=True, verbose_name='Текст статьи:') # указание creditor в самой модели
    post_like = models.IntegerField(default=0)
    post_created_date = models.DateTimeField(default=timezone.now)
    post_public_date = models.DateTimeField(blank=True, null=True)

    def public(self):
        self.post_public_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.post_title


class Comments(models.Model):
    class Meta:
        db_table = 'comments'
    comments_text = models.TextField(verbose_name='Текст комментария')
    comments_post = models.ForeignKey(Post)

    def __unicode__(self):
        return self.comments_text

