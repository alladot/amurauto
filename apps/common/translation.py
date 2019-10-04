# -*- coding: utf-8 -*-
from modeltranslation.translator import register, TranslationOptions

from common.models import IndexPageText


@register(IndexPageText)
class IndexPageTextTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Текст.
    """
    fields = (
        'title',
        'content',
    )
