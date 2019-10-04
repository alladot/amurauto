# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.messages import info
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import settings
from mezzanine.conf.admin import SettingsAdmin
from mezzanine.conf.models import Setting
from mezzanine.utils.static import static_lazy as static

from common.forms import SettingsForm
from common.models import IndexPagePicture, IndexPageText


class TranslatableSettingsAdmin(SettingsAdmin):
    """
    Настройки с отображением мультиязычных значений.
    Поправка по классу SettingsAdmin - корректное указание путей к js
    """
    class Media(SettingsAdmin.Media):
        js = [
            js.replace(
                str(static(
                    "mezzanine/js/admin/tabbed_translation_fields.js")),
                str(static(
                    "mezzanine/js/admin/tabbed_translatable_settings.js"))
            ) for js in SettingsAdmin.Media.js
        ]

    def changelist_view(self, request, extra_context=None):
        if not extra_context:
            extra_context = {}
        settings_form = SettingsForm(request.POST or None)
        if settings_form.is_valid():
            settings_form.save()
            settings.clear_cache()
            info(request, _("Settings were successfully updated."))
            return self.changelist_redirect()
        extra_context["settings_form"] = settings_form
        extra_context["title"] = u"%s %s" % (
            _("Change"), force_text(Setting._meta.verbose_name_plural))
        return super(SettingsAdmin, self).changelist_view(
            request, extra_context)


class IndexPagePictureAdmin(ModelAdmin):
    """
    Картинки на главной странице
    """
    fields = (
        'file',
        'position',
        'font_color',
    )
    list_display = [
        'admin_thumb',
        'position',
    ]
    list_display_links = ('admin_thumb',)
    list_editable = ('position',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        """
        Используем кастомный виджет для поля font_color
        """
        from common.widgets import ColorPickerWidget
        if db_field.name == 'font_color':
            kwargs['widget'] = ColorPickerWidget
        return super(IndexPagePictureAdmin, self).formfield_for_dbfield(
            db_field, **kwargs)


class IndexPageTextAdmin(ModelAdmin):
    """
    Тексты на главной странице
    """
    fields = (
        'code',
        'title',
        'content',
    )
    list_display = [
        'code',
        'title',
        'content',
    ]
    list_display_links = ('code', 'title',)
    list_editable = ()


admin.site.register(IndexPagePicture, IndexPagePictureAdmin)
admin.site.register(IndexPageText, IndexPageTextAdmin)
admin.site.unregister(Setting)
admin.site.register(Setting, TranslatableSettingsAdmin)
