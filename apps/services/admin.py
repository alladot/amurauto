# -*- coding: utf-8 -*-
from django.contrib import admin
from mezzanine.core.admin import BaseTranslationModelAdmin

from services.models import Service


class ServiceAdmin(BaseTranslationModelAdmin):
    """
    Шаблонная "карточка" услуги
    """
    fieldsets = (
        (None, {
            'fields': [
                'order',
                'title',
                'content',
                'icon_name',
            ]
        }),
    )
    list_display = [
        'order', 'title', 'content'
    ]
    list_display_links = ('title',)


admin.site.register(Service, ServiceAdmin)
