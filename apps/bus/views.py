# -*- coding: utf-8 -*-
from django.views import generic
from mezzanine.conf import settings

from bus.models import Bus


class BusListView(generic.ListView):
    """
    Список автобусов
    """
    model = Bus
    template_name = 'project/project_list.html'

    def get_paginate_by(self, queryset):
        return settings.SITE_TILE_PAGINATION

    def get_queryset(self):
        """
        Возвращает полный список опубликованных автобусов;
        :return: список автобусов
        :rtype: QuerySet
        """
        buses = Bus.objects.published()
        return buses


class BusDetailView(generic.DetailView):
    """
    Описание автобуса
    """
    model = Bus
    template_name = 'project/project_detail.html'
