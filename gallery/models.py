#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

# Альбом с фотографиями

class Album(models.Model):
    class Meta:
        db_table = 'db_album_gallery_app'
        ordering = ['title']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
    title = models.CharField("Название фотографии", max_length=100, blank=True)
    slug = models.SlugField("Ссылка для альбома", max_length=100, unique=True)
    img = models.ImageField("Изображение альбома", upload_to='images',
                            help_text='Изображение 200px на 200px', blank=True)

    def __unicode__(self):
        return self.title
        
        
# Фотографии в альбоме

class Photo(models.Model):
    class Meta:
        db_table = 'db_photo_gallery_app'
        ordering = ['title']
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
    title = models.CharField('Название фотографии', max_length=100, blank=True)
    album = models.ForeignKey(Album, verbose_name='Альбом')
    img = models.ImageField('Фото', upload_to='images', 
                            help_text= 'Желательно, чтоб фото было не большого размера')
    
    
    def __unicode__(self):
        return self.title