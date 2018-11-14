# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import force_text
from mezzanine.core.fields import FileField
from mezzanine.utils.models import upload_to, AdminThumbMixin

from common import validators


class IndexPagePicture(AdminThumbMixin, models.Model):
    """
    Модель изображений, используемых на главной странице
    """
    MAIN = 'MAIN'
    FAKE = 'FAKE'

    POSITIONS = ((MAIN, 'Главное изображение'),
                 (FAKE, 'Не используется')
                 )

    file = FileField(
        verbose_name='Изображение', max_length=500, format='Image',
        upload_to=upload_to('common.IndexPagePicture.file', 'index_picture'))
    position = models.CharField(
        verbose_name='Где используется', choices=POSITIONS, default=FAKE,
        blank=False, null=False, max_length=50)
    font_color = models.CharField(
        verbose_name='Цвет текста',
        help_text='Цвет текста в формате #rrggbb',
        validators=[validators.HexColorValidator()],
        max_length=7, blank=True, null=True
    )

    admin_thumb_field = 'file'

    class Meta:
        verbose_name = 'Картинка на главной'
        verbose_name_plural = 'Картинки на главной'

    def __str__(self):
        name = force_text(self.file)
        name = name.rsplit('/', 1)[-1]
        return name
