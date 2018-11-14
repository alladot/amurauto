# -*- coding: utf-8 -*-
from django.contrib import admin
from mezzanine.core.admin import BaseTranslationModelAdmin

from reviews.models import Review


class ReviewAdmin(BaseTranslationModelAdmin):
    """
    Шаблонная "карточка" отзыва
    """
    fieldsets = (
        (None, {
            'fields': [
                'title',
                'is_company',
                'photo',
                'content',
            ]
        }),
    )
    list_display = [
        'title', 'admin_thumb', 'is_company', 'content',
    ]
    list_display_links = ('title', 'admin_thumb',)


admin.site.register(Review, ReviewAdmin)
