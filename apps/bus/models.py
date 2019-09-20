# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable
from mezzanine.core.models import RichText
from mezzanine.utils.models import AdminThumbMixin
from mezzanine.utils.models import upload_to


def get_year():
    """
    Получить текущий год
    """
    return timezone.now().year


class Bus(Displayable, RichText, AdminThumbMixin):
    """
    Модель автобус
    """
    photo = FileField(
        verbose_name='Фото',
        upload_to=upload_to('bus.Bus.photo', 'bus_photo'),
        format='Image', max_length=255, null=True, blank=True)
    year = models.SmallIntegerField(
        verbose_name='Год выпуска',
        default=get_year, blank=True, null=True)
    capacity = models.SmallIntegerField(
        verbose_name='Количество мест', blank=True, null=True)
    cost_per_hour = models.FloatField(
        verbose_name='Стоимость в час', blank=True, null=True)
    min_hours = models.FloatField(
        verbose_name='Минимальный заказ, часов', blank=True, null=True)
    order = models.IntegerField(
        'Порядковый номер', null=True)

    admin_thumb_field = 'photo'

    class Meta:
        verbose_name = 'Автобус'
        verbose_name_plural = 'Автобусы'
        ordering = ('order', 'title',)

    def get_absolute_url(self):
        return reverse(
            'bus:detail', kwargs={'slug': self.slug}
        )


Bus._meta.get_field('title').verbose_name = 'Наименование'
Bus._meta.get_field('content').verbose_name = 'Описание'


class BusPhoto(models.Model):
    """
    Модель фотографий автобуса
    """
    bus = models.ForeignKey(Bus, related_name='other_photos')
    photo = FileField(
        verbose_name='Фотография автобуса', max_length=200, format='Image',
        upload_to=upload_to('bus.Bus.photo_gallery', 'bus_photo_gallery')
    )

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
