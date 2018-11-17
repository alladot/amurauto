# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include
#from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
#from mezzanine.core.views import direct_to_template
from mezzanine.pages.views import page

#from common.views import set_language

ADMIN_PREFIX = 'admin'
admin.autodiscover()

urlpatterns = [
    #url(r'^i18n/setlang/$', set_language, name='set_language'),
    #url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^{admin_prefix}/'.format(admin_prefix=ADMIN_PREFIX), include(
        admin.site.urls)),
]

# if 'rosetta' in settings.INSTALLED_APPS:
#     urlpatterns += [
#         url(r'^admin/rosetta/', include('rosetta.urls'))
#     ]

#urlpatterns += i18n_patterns(
urlpatterns += [
    url(r'^$', page, {'slug': '/'}, name='home'),
    url(r'^bus/', include('bus.urls', namespace='bus')),
    url(r'^', include('mezzanine.urls')),
]

handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
