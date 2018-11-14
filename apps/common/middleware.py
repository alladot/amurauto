# -*- coding: utf-8 -*-
from mezzanine.conf import settings
from django.utils import translation

from urls import ADMIN_PREFIX


class AdminLocaleMiddleware:
    """
    Административная панель всегда отображается на основном языке
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/{admin_prefix}'.format(admin_prefix=ADMIN_PREFIX)):
            request.LANG = getattr(settings, 'ADMIN_LANGUAGE_CODE', settings.LANGUAGE_CODE)
            translation.activate(request.LANG)
            request.LANGUAGE_CODE = request.LANG
        response = self.get_response(request)
        return response
