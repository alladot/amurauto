# -*- coding: utf-8 -*-
from django.db import models


class Service(models.Model):
    """
    Модель услуги
    """
    title = models.CharField(
        'Название услуги', blank=False, null=False, max_length=100)
    content = models.TextField(
        'Описание', blank=True, null=False, max_length=300)
    icon_name = models.CharField(
        'Название иконки', blank=True, null=True, max_length=30)
    order = models.IntegerField(
        'Порядковый номер', null=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ('order', 'title',)
