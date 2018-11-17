# -*- coding: utf-8 -*-
from modeltranslation.translator import register, TranslationOptions

from benefits.models import Benefit


@register(Benefit)
class BenefitTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Преимущество.
    """
    fields = (
        'title',
        'content',
    )
