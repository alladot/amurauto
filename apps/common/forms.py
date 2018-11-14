# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import activate, get_language
from future.builtins import int
from mezzanine.conf import settings, registry, forms as mezzanine_forms
from mezzanine.conf.models import Setting

if settings.USE_MODELTRANSLATION:
    from collections import OrderedDict
    from modeltranslation.utils import build_localized_fieldname

# from common.models import PhoneNumber


FIELD_TYPES = {
    bool: forms.BooleanField,
    int: forms.IntegerField,
    float: forms.FloatField,
}


class SettingsForm(mezzanine_forms.SettingsForm):
    """
    Форма для настроек с отображением мультиязычных значений.
    Исправление работы класса SettingsForm - корректное сохранение и загрузка
    значений в поля
    """

    def __init__(self, *args, **kwargs):
        super(mezzanine_forms.SettingsForm, self).__init__(*args, **kwargs)
        # Создает поля формы соответствующего типа для каждой редактируемой
        #  настройки, кроме перечисленных в ADMIN_REMOVAL_SETTINGS
        active_language = get_language()
        names = (name for name in sorted(registry.keys())
                 if name not in settings.ADMIN_REMOVAL_SETTINGS)
        for name in names:
            setting = registry[name]
            if setting["editable"]:
                field_class = FIELD_TYPES.get(setting["type"], forms.CharField)
                if settings.USE_MODELTRANSLATION and setting["translatable"]:
                    self._init_translatable_field(setting, field_class, name)
                else:
                    self._init_field(setting, field_class, name)
        activate(active_language)

    def _init_translatable_field(self, setting, field_class, name):
        """
        Инициализация мультиязычного поля с соответствующими именами
         для каждой локализации
        :param setting: настройка из registry[]
        :param field_class: тип поля для данной настройки
        :param name: имя настройки
        """
        obj = None
        try:
            obj = Setting.objects.get(name=name)
        except Setting.DoesNotExist:
            pass

        for code in OrderedDict(settings.LANGUAGES):
            try:
                activate(code)
            except IOError:
                pass
            else:
                self._init_field(setting, field_class, name, code, obj)

    def _init_field(self, setting, field_class, name, code=None, obj=None):
        """
        Инициализация поля с именем для локализации,
        либо без, если локализации нет (code=None)
        :param setting: настройка из registry[]
        :param field_class: тип поля для данной настройки
        :param name: имя настройки
        :param code: языковой код
        :param obj: объект модели Setting для данной настройки (если найден)
        """
        initial = getattr(settings, name)
        if obj and code:
            initial = getattr(obj, "value_{lang}".format(lang=code))

        kwargs = {
            "label": setting["label"] + ":",
            "required": setting["type"] in (int, float),
            "initial": initial,
            "help_text": self.format_help(setting["description"]),
        }

        if setting["choices"]:
            field_class = forms.ChoiceField
            kwargs["choices"] = setting["choices"]
        field_instance = field_class(**kwargs)
        code_name = ('_modeltranslation_' + code if code else '')
        self.fields[name + code_name] = field_instance
        css_class = field_class.__name__.lower()
        field_instance.widget.attrs["class"] = css_class
        if code:
            field_instance.widget.attrs["class"] += " modeltranslation"

    def save(self):
        """
        Сохранение настроек в БД.
        """
        active_language = get_language()
        for (name, value) in self.cleaned_data.items():
            if name not in registry:
                name, code = name.rsplit('_modeltranslation_', 1)
            else:
                code = None
            setting_obj, created = Setting.objects.get_or_create(name=name)
            if settings.USE_MODELTRANSLATION:
                if registry[name]["translatable"]:
                    attr_name = "value_{lang}".format(lang=code)
                    try:
                        activate(code)
                    except IOError:
                        pass
                    finally:
                        if hasattr(setting_obj, attr_name):
                            setattr(setting_obj, attr_name, value)
                        activate(active_language)
                else:
                    # Дублирование значения в каждое поле для всех локализаций
                    for code in OrderedDict(settings.LANGUAGES):
                        setattr(setting_obj, build_localized_fieldname(
                            'value', code), value)
            else:
                setting_obj.value = value
            setting_obj.save()


# class PhoneForm(forms.ModelForm):
#     """
#     Форма телефона c кастомной маской, используется jQuery-Mask-Plugin.
#     Маска задается в атрибутах виджета параметром `data-mask'
#
#     .. _jQuery-Mask-Plugin:
#        https://igorescobar.github.io/jQuery-Mask-Plugin/docs.html
#        https://github.com/igorescobar/jQuery-Mask-Plugin
#     """
#     class Meta:
#         model = PhoneNumber
#         widgets = {
#             'phone': forms.TextInput(
#                 attrs={
#                     'class': 'vTextField',
#                     'data-mask': '+0 (000) 000-00-00-000000000'
#                 },
#
#             ),
#         }
#         fields = ('phone',)
#
#
# class SearchForm(forms.Form):
#     """
#     Форма поиска
#     """
#     search = forms.CharField(
#         label=_('Title'),
#         widget=forms.TextInput(attrs={
#             'placeholder': _('Искать по наименованию')
#         })
#     )
