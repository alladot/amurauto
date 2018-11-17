# -*- coding: utf-8 -*-
from modeltranslation.translator import register, TranslationOptions

from reviews.models import Review


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Отзыв.
    """
    fields = (
        'title',
        'content',
    )
