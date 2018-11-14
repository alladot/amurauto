# -*- coding: utf-8 -*-
from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible


# @deconstructible
# class PhoneValidator(RegexValidator):
#     """
#      Валидатор номера телефона
#     """
#     regex = r'^\+\d\s\([0-9]{3}\)\s[0-9]{3}(-[0-9]+){2}(-[0-9]{1,9})?$'
#     message = ("Телефонный номер должен быть введен в формате: "
#                "'+0 (000) 000-00-00'. Допускается до 20 цифр.")
#
#     def __init__(self, **kwargs):
#         super(PhoneValidator, self).__init__(**kwargs)
#
#     def __call__(self, value):
#         super(PhoneValidator, self).__call__(value)


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
