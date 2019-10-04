# -*- coding: utf-8 -*-
from django.core.exceptions import FieldDoesNotExist
from mezzanine import template
from common.models import IndexPageText


register = template.Library()


@register.filter
def text_get(code, field):
    """Получить значение поля fileld из объекта IndexPageText с кодом code.

    :param code: код
    :param field: получаемое поле
    :return: значение поля, либо None в случае отсутствия поля с таким
    названием в модели IndexPageText, или отсутствия объекта с кодом code
    """
    try:
        IndexPageText._meta.get_field(field)
        indexPageText = IndexPageText.objects.filter(code=code)
        if indexPageText and len(indexPageText) > 0:
            return getattr(indexPageText[0], field)
    except FieldDoesNotExist:
        pass

    return None
