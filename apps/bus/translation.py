# -*- coding: utf-8 -*-
from modeltranslation.translator import register, TranslationOptions

from bus.models import Bus


@register(Bus)
class BusTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Автобус
    """
    fields = (
        'title',
        'content',
    )
