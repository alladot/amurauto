# -*- coding: utf-8 -*-
from django.db import models
from mezzanine.core.fields import FileField
from mezzanine.utils.models import AdminThumbMixin
from mezzanine.utils.models import upload_to


class Review(models.Model, AdminThumbMixin):
    """
    Модель отзыва
    """
    title = models.CharField(
        'Автор отзыва', blank=False, null=False, max_length=100)
    is_company = models.BooleanField(
        'Организация', blank=False, null=False, default=False)
    photo = FileField(
        verbose_name='Логотип или фото',
        upload_to=upload_to('reviews.Review.photo', 'review_photo'),
        format='Image', max_length=255, null=True, blank=True)
    content = models.TextField(
        'Описание', blank=False, null=False, max_length=500)

    admin_thumb_field = 'photo'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-is_company', 'title',)
