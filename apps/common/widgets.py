# -*- coding: utf-8 -*-
from django import forms
from django.utils.html import mark_safe


class ColorPickerWidget(forms.widgets.TextInput):
    """
    Виджет для выбора цвета с использованием farbtastic
    """
    class Media:
        css = {
            'all': ('/static/vendor/farbtastic/farbtastic.css',)
            }
        js = ('/static/vendor/jquery/jquery.js',
              '/static/vendor/farbtastic/colorpicker.js',
              '/static/vendor/farbtastic/farbtastic.js',
              )

    def render(self, name, value, attrs=None):
        text_input_html = super(ColorPickerWidget, self).render(
            name, value, attrs)
        return mark_safe(text_input_html)
