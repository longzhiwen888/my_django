#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to my site.")


def static_view(request, path):
    return HttpResponse("path:%s" % path)
