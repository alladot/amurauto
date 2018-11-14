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
                'title',
                'content',
                'icon_name',
            ]
        }),
    )
    list_display = [
        'title', 'content',
    ]
    list_display_links = ('title',)


admin.site.register(Benefit, BenefitAdmin)
