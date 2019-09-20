# -*- coding: utf-8 -*-
from django.db import models


class Benefit(models.Model):
    """
    Модель преимущество
    """
    title = models.CharField(
        'Название преимущества', blank=False, null=False, max_length=100)
    content = models.TextField(
        'Описание', blank=False, null=False, max_length=300)
    icon_name = models.CharField(
        'Название иконки', blank=True, null=True, max_length=30)
    order = models.IntegerField(
        'Порядковый номер', null=True)

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
        ordering = ('order', 'title',)
