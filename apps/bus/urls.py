# -*- coding: utf-8 -*-
from django.conf.urls import url

from bus.views import BusDetailView
from bus.views import BusListView

urlpatterns = [
    url(r'^$', BusListView.as_view(), name='list'),
    url(r'^(?P<slug>.*)$', BusDetailView.as_view(), name='detail'),
]
