# -*- coding: utf-8 -*-
from modeltranslation.translator import register, TranslationOptions

from benefits.models import Benefit


@register(Benefit)
class ServiceTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Преимущество.
    """
    fields = (
        'title',
        'content',
    )
