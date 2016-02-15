#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Clients(models.Model):
    class Meta:
        db_table = 'db_clients_app'
        verbose_name = 'Клиентская база'
        ordering = ['number']
    name = models.CharField(max_length=200, verbose_name='Имя клиента', blank=True)
    number = models.CharField(max_length=200, verbose_name='Номер телефона', blank=True, unique=True, 
                              help_text='номер в формате 0504824567')
    formula = models.TextField(verbose_name='Формула окраски клиента', blank=True)
    
    
    def __unicode__(self):
        return self.name
        
class Search(models.Model):
    class Meta:
        db_table = 'db_clients_search'
        verbose_name = 'Поиск клиентов'
    number = models.CharField(max_length=200, verbose_name='Номер телефона', blank=True,
                              help_text='номер в формате 0504824567')
    
