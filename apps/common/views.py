# -*- coding: utf-8 -*-
from django import http
from django.conf import settings
from django.urls import translate_url
from django.utils.http import is_safe_url, urlunquote
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.utils.translation import check_for_language

LANGUAGE_QUERY_PARAMETER = 'language'


def set_language(request):
    """
    Переопределение представления views.i18n.set_language
     для смены языка и перехода по ссылке не только для
     метода POST, но также и для GET.
     Перенаправляет на заданный url с установлением выбранного
     языка в сессии или куки. Url и код языка должны быть указаны
     в параметрах запроса.
    """
    next = request.POST.get('next', request.GET.get('next'))
    if (next or not request.is_ajax()) and not is_safe_url(
            url=next, host=request.get_host()):
        next = request.META.get('HTTP_REFERER')
        if next:
            next = urlunquote(next)  # HTTP_REFERER may be encoded.
        if not is_safe_url(url=next, host=request.get_host()):
            next = '/'
    response = http.HttpResponseRedirect(next) if next else http.HttpResponse(
        status=204)
    lang_code = request.POST.get(LANGUAGE_QUERY_PARAMETER,
                                 request.GET.get(LANGUAGE_QUERY_PARAMETER))
    if lang_code and check_for_language(lang_code):
        if next:
            next_trans = translate_url(next, lang_code)
            if next_trans != next:
                response = http.HttpResponseRedirect(next_trans)
        if hasattr(request, 'session'):
            request.session[LANGUAGE_SESSION_KEY] = lang_code
        else:
            response.set_cookie(
                settings.LANGUAGE_COOKIE_NAME, lang_code,
                max_age=settings.LANGUAGE_COOKIE_AGE,
                path=settings.LANGUAGE_COOKIE_PATH,
                domain=settings.LANGUAGE_COOKIE_DOMAIN,
            )
    return response
