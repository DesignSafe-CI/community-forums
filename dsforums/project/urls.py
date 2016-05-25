# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http.response import HttpResponseRedirect

import spirit.urls
import ds_auth.urls

# Override admin login for security purposes
from django.contrib.auth.decorators import login_required
admin.site.login = login_required(admin.site.login)


urlpatterns = [
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^example/', include('example.foo.urls')),
    url(r'^login/$', lambda request: HttpResponseRedirect('/auth?' + request.GET.urlencode())),
    url(r'^user/login/$', lambda request: HttpResponseRedirect('/auth?' + request.GET.urlencode())),
    url(r'^register/$', lambda request: HttpResponseRedirect('https://www.designsafe-ci.org/register')),
    url(r'^user/register/$', lambda request: HttpResponseRedirect('https://www.designsafe-ci.org/register')),
    url(r'^auth/', include(ds_auth.urls, namespace='ds_auth', app_name='ds_auth')),
    url(r'^', include(spirit.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
