# -*- coding: utf-8 -*-
from django.contrib import admin
from mezzanine.core.admin import BaseTranslationModelAdmin

from documents.models import Document


class DocumentAdmin(BaseTranslationModelAdmin):
    """
    Шаблонная "карточка" документа
    """
    fieldsets = (
        (None, {
            'fields': [
                'caption',
                'image',
            ]
        }),
    )
    list_display = [
        'caption', 'image',
    ]
    list_display_links = ('caption', 'image',)


admin.site.register(Document, DocumentAdmin)
