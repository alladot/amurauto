# -*- coding: utf-8 -*-
import math
# from django.core.urlresolvers import reverse
# from django.template import Context, TemplateSyntaxError, Variable
# from django.template.loader import get_template
# from mezzanine.pages.models import Page
from django.utils.translation import ugettext as _
from mezzanine import template

# from common.utils.dominant_color import image_to_dominant_color_create


register = template.Library()

#
# @register.simple_tag
# def hours(amount):
#     """Формирует подпись "часов" в нужном падеже
#
#     :param amount: количество часов, к которому формируется подпись
#     :return: подпись "часов"
#     :rtype: str
#     """
#     result = None
#     try:
#         amount = float(amount)
#     except ValueError:
#         return result
#     result = (
#         _('час') if math.fmod(amount, 10) == 1.0 else
#         _('часов') if math.fmod(amount, 10) in (1.0 else


# def chunked(iterable, count_parts):
#     """Разделяет iterable на ``count_parts`` частей"""
#     chunk_size = int(math.ceil(len(iterable) / count_parts))
#     return (iterable[i * chunk_size:i * chunk_size + chunk_size]
#             for i in range(count_parts))
#
#
# @register.render_tag
# def footer_menu_columned(context, token):
#     """Возвращает включенные для заданного шаблона меню страницы без иерархии
#
#     поделенные на заданное количество списков
#
#     :param context: Контекст
#     :param token: Должно содержать имя шаблона меню (строка),
#      количество колонок (целочисленное, по умоланию 2)
#     :return: список из count_parts списков страниц для отображения в меню
#     :rtype: list of count_parts lists of Page
#     """
#     # Задаем по умолчанию деление на 2 колонки:
#     count_parts = 2
#     parts = token.split_contents()[1:]
#     # Выделяем из parts имя шаблона и количество колонок
#     for part in parts:
#         # Связываем с контекстом для получения значения, заданного в шаблоне
#         part = Variable(part).resolve(context)
#         if isinstance(part, str):
#             template_name = part
#         if isinstance(part, int):
#             count_parts = part
#     if not template_name:
#         try:
#             template_name = context["menu_template_name"]
#         except KeyError:
#             error = (
#                 "Не найден шаблон для меню подвала в: {parts}"
#             ).format(parts=parts)
#             raise TemplateSyntaxError(error)
#     context["menu_template_name"] = template_name
#     menu_list = []
#     for page in Page.objects.published().order_by("_order"):
#         if page.in_menu_template(template_name):
#             menu_list.append(page)
#     context["menu_lists"] = chunked(menu_list, count_parts)
#     template = get_template(template_name)
#     return template.render(Context(context))
#
#
# @register.simple_tag()
# def logo_to_custom_color(file_, size=None, color=None):
#     """Возвращает исходное изображение дополненное до заданного размера, либо
#      до квадратного (если размеры не указаны).
#
#      Также заливает изображение:
#       по умолчанию доминантным цветом,
#       либо цветом указанным в `color`.
#
#     :param file_: путь до исходного изображения
#     :param size: размер в пикселях, строка вида "100x50". Если параметр не
#      указан, или указаны не оба размера, то получаем квадрат со стороной большей
#       размерности исходного изображения.
#     :param color: строка вида "255,255,255" для RGB,
#     строка вида "255,255,255,255" для RGBA
#     :return: путь до преобразованного изображения
#     :rtype: str
#     """
#     width = 0
#     height = 0
#     if size:
#         width_str, height_str = size.split('x', 1)
#         try:
#             width = int(width_str) if int(width_str) > 0 else 0
#             height = int(height_str) if int(height_str) > 0 else 0
#         except ValueError:
#             width = 0
#             height = 0
#
#     if color:
#         try:
#             color = tuple([int(val) for val in color.split(',')])
#         except ValueError:
#             color = None
#
#     return image_to_dominant_color_create(file_, width, height, color)
#
#
# @register.simple_tag
# def get_competency_url(competence, namespace):
#     """Формирует url для отображения компетенции
#
#     в соответствующем пространстве имен (организация, эксперт или проект)
#
#     :param competence: объект Компетенция
#     :param namespace: строка с названием пространства имен:
#      'company', 'expert' или 'project'
#     :return: ссылка на компетенцию в заданном пространстве имен
#     :rtype: str
#     """
#     return reverse(
#         "{namespace}:competence".format(namespace=namespace),
#         kwargs={'competence': competence.slug}
#     )
#
#
# @register.filter(name='class_name')
# def get_class_name(value):
#     """Возвращает имя класса"""
#     return value.__class__.__name__
#
#
# @register.inclusion_tag("includes/querystring.html", takes_context=True)
# def other_querystring(context, exclude_var, has_first_var=True):
#     """Возвращает строковый список параметров из словаря request.GET
#
#     без элемента exclude_var. Используется для построения url в случаях, когда
#     используется несколько параметров, и изменение одного из них не должно
#     затирать остальные.
#     Параметр page исключаем принудительно, т.к. номер страницы перестает быть
#      актуальным при изменении условий фильтрации.
#     Пример: текущий url /mypage/?param1=1&param2=2 и необходимо сгенерировать
#      url с новым значением param1, при этом сохраняя условие param2
#      Использование в шаблоне:
#      <a href="?param1=3{% other_querystring "param1" %}">
#      Получится url /mypage/?param1=3&param2=2
#     :param context: контекст шаблона
#     :param exclude_var: наименование исключаемого параметра
#     :param has_first_var: передается в шаблон и регулирует,
#      будет ли строка начинаться с ? (в случае True) или &
#     :return: строка параметров для url и значение has_first_var
#     """
#     page_var_name = 'page'
#     querystring = context["request"].GET.copy()
#     if exclude_var:
#         exclude_vars = [exclude_var]
#         for exclude_var in exclude_vars:
#             if exclude_var in querystring:
#                 del querystring[exclude_var]
#     if page_var_name in querystring:
#         del querystring[page_var_name]
#     querystring = querystring.urlencode()
#     return {
#         'querystring': querystring,
#         'has_first_var': has_first_var,
#     }
#
#
# @register.filter
# def get_item(dictionary, key):
#     """Получить элемент словаря по переданному ключу.
#
#     :param dictionary: словарь
#     :param key: ключ
#     :return: элемент словаря, либо None в случае отсутствия ключа в словаре
#     """
#     return dictionary.get(key, None)
