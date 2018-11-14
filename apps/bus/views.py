# -*- coding: utf-8 -*-
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import generic
from mezzanine.conf import settings

# from common.mixins import SearchFormMixin
# from common.models import Competence
from bus.models import Bus


class BusListView(generic.ListView):
    #, SearchFormMixin
    """
    Список автобусов
    """
    model = Bus
    template_name = 'project/project_list.html'

    def get_paginate_by(self, queryset):
        return settings.SITE_TILE_PAGINATION

    def get_queryset(self):
        """
        Возвращает список проектов с учетом переданного параметра:
         по умолчанию: полный список опубликованных проектов;
         competence: проекты, у которых есть данная компетенция.
        :return: список проектов
        :rtype: QuerySet
        """
        buses = Bus.objects.published()
        # if 'competence' in self.kwargs:
        #     slug = self.kwargs['competence']
        #     competence = get_object_or_404(Competence, slug=slug)
        #     projects = projects.filter(competencies=competence)
        #
        # query = self.request.GET.get('search')
        # if query:
        #     projects = projects.filter(
        #         Q(title__icontains=query) |
        #         Q(content__icontains=query))

        return buses

    # def get_context_data(self, **kwargs):
    #     """
    #     Добавляет в контекст все компетенции с подсчетом количества проектов
    #     """
    #     context = super(ProjectListView, self).get_context_data(**kwargs)
    #     competence = None
    #     if 'competence' in self.kwargs:
    #         competence = get_object_or_404(Competence, slug=self.kwargs['competence'])
    #     context.update({
    #         'current_competence': competence,
    #         'competencies': Competence.objects.annotate(count=Count('project')).filter(count__gt=0),
    #     })
    #     return context


class BusDetailView(generic.DetailView):
    """
    Описание автобуса
    """
    model = Bus
    template_name = 'project/project_detail.html'

    # def get_context_data(self, **kwargs):
    #     """
    #     Добавляет в контекст компании, экспертов и изображения проекта,
    #      а также все компетенции с подсчетом количества проектов
    #     """
    #     context = super(ProjectDetailView, self).get_context_data(**kwargs)
    #     context.update({
    #         'photos': ProjectImage.objects.filter(project__pk=self.object.pk),
    #         'companies':
    #             Company.objects.published().filter(projects=self.object),
    #         'experts': Expert.objects.published().filter(project=self.object),
    #         'supports': Support.objects.published().filter(project=self.object),
    #         'competencies': Competence.objects.annotate(count=Count('project')).filter(count__gt=0),
    #     })
    #     return context
