# -*- coding: utf-8 -*-

from modeltranslation.translator import register, TranslationOptions

from documents.models import Document


@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Документ.
    """
    fields = (
        'caption',
    )
