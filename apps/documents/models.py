# -*- coding: utf-8 -*-
from django.db import models
from mezzanine.core.fields import FileField
from mezzanine.utils.models import upload_to, AdminThumbMixin


class Document(models.Model, AdminThumbMixin):
    """
    Модель документа
    """
    image = FileField(
        verbose_name='Изображение',
        upload_to=upload_to('docs', 'docs'),
        format='Image', max_length=255, null=False, blank=False)
    caption = models.CharField(
        verbose_name='Наименование', blank=False, null=False, max_length=150)

    admin_thumb_field = 'image'

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ('caption',)
