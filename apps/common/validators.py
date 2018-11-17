# -*- coding: utf-8 -*-
from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class HexColorValidator(RegexValidator):
    """
    Валидатор шестнадцатеричного значения цвета
    """
    regex = r'^#[0-9a-fA-F]{6}$'
    message = ("Значение цвета должно быть в формате #ffffff "
               "(6 символов 0-9, a-f)")

    def __init__(self, **kwargs):
        super(HexColorValidator, self).__init__(**kwargs)

    def __call__(self, value):
        super(HexColorValidator, self).__call__(value)
