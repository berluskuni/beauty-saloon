#-*- coding: utf-8 -*-
from django.db import models


class Photo(models.Model):
    class Meta:
        db_table = 'db_salon_interior'
        ordering = ['title']
        verbose_name = 'Фото'
        verbose_name_plural = "Фотографии"
    index = models.IntegerField(default=0, verbose_name='Индекс')
    title = models.CharField("Название фотографии", max_length=100, blank=True)
    alt = models.TextField(verbose_name='Подсказка', blank=True)
    img = models.ImageField("Фото", upload_to='uploads',
	                       help_text='Желательно, чтоб фото было не большого размера')
    img_litle = models.ImageField(verbose_name='200x200', upload_to='uploads',
	                       help_text='Желательно, чтоб фото было не большого размера', blank=True)
   

	
	
    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
        return '/static/media/uploads/%s' % self.img
        
    def get_absolute_url(self):
        return '/static/media/uloads/%s' % self.img_litle
        
        
        
        
class PhotoTh(models.Model):
    class Meta:
        db_table = 'db_salon_interior_th'
        ordering = ['title']
        verbose_name = 'Фото_200*200'
        verbose_name_plural = "Фотографии_200*200"
    index = models.IntegerField(default=0, verbose_name='Индекс')
    title = models.CharField("Название фотографии", max_length=100, blank=True)
    alt = models.TextField(verbose_name='Подсказка', blank=True)
    img_th = models.ImageField("Фото", upload_to='uploads',
	                       help_text='Желательно, чтоб фото было не большого размера')

	
	
    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
        return '/static/media/uploads/%s' % self.img_th
