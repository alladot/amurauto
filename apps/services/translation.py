# -*- coding: utf-8 -*-

from modeltranslation.translator import register, TranslationOptions

from services.models import Service


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Услуга.
    """
    fields = (
        'title',
        'content',
    )
