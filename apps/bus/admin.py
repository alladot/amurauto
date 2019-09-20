# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.admin import BaseTranslationModelAdmin

from bus.models import BusPhoto
from bus.models import Bus


class BusPhotoInline(admin.TabularInline):
    """
    Фотографии автобуса
    """
    model = BusPhoto
    extra = 1


class BusAdmin(BaseTranslationModelAdmin):
    """
    Автобус
    """
    fieldsets = (
        (None, {
            'fields': [
                'order',
                'photo',
                'title',
                'year',
                'capacity',
                'cost_per_hour',
                'min_hours',
                ('publish_date', 'expiry_date'),
                'status',
                'content'
            ]
        }),
        (_("Meta data"), {
            "fields": [
                '_meta_title', 'slug',
                ('description', 'gen_description'),
                'keywords', 'in_sitemap'
            ],
            "classes": ("collapse-closed",)
        }),

    )
    list_display = [
        'order', 'admin_thumb', 'title', 'year',
        'status', 'admin_link'
    ]
    list_display_links = ('title', 'admin_thumb')
    prepopulated_fields = {'slug': ('title',)}

    inlines = (BusPhotoInline,)


admin.site.register(Bus, BusAdmin)
