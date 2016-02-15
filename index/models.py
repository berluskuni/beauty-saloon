#-*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField


class CkEditor(models.Model):
    class Meta:
        db_table = 'test_cseditor'
    title = models.CharField(blank=True, max_length=200)
    text_ck = RichTextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.title
        
class AboutMe(models.Model):
    class Meta:
        db_table = 'salon_about_my'
    title = models.CharField(blank=True, max_length=200, verbose_name='моё имя')
    about_me = RichTextField(blank=True, null=True, verbose_name='обо мне')
    public_date = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    


