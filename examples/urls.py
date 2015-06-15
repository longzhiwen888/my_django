#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from examples import views

urlpatterns = patterns(
    '',
    url(r'document/preview/(\d+)/$', views.document_preview,
        name='document_preview'),
    url(r'comment/preview/(\d+)/$', views.comment_preview,
        name='comment_preview'),
)
