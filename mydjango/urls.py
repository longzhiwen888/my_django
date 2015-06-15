#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^$', 'mydjango.views.welcome'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^examples/', include('examples.urls')),
    url(r'^search/', include('haystack.urls')),
]

if not settings.DEBUG:
    urlpatterns.append(url(
        r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT
         }))

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

# print dir(urlpatterns[1])
# print '*' * 100
# print urlpatterns[1].__dict__
# print '*' * 100
# print 'urlpatterns[1].namespace_dict:%s' % urlpatterns[1].namespace_dict
#
# for child in urlpatterns[1].urlconf_name:
#     print child, dir(child)
#     print child.__dict__