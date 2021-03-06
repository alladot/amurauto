# -*- coding: utf-8 -*-
from django.contrib import admin
from mezzanine.core.admin import BaseTranslationModelAdmin

from benefits.models import Benefit


class BenefitAdmin(BaseTranslationModelAdmin):
    """
    Шаблонная "карточка" преимущества
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
        'order', 'title', 'content',
    ]
    list_display_links = ('title',)


admin.site.register(Benefit, BenefitAdmin)
