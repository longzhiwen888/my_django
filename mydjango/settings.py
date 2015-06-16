#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Django settings for mydjango project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_WEB_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1_i+zajc$xmtiwx4jsn3plb+squ&cgip)-$-3szj8r-83e3f84'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']



# Application definition

INSTALLED_APPS = (
    'inventory',
    # 'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    # 'bootstrap_admin',
    # 'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'examples',
    'haystack',
    'debug_toolbar',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'mydjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
TEMPLATE_DIRS = (
    os.path.join(MAIN_WEB_ROOT_DIR, 'templates'),
    os.path.join(BASE_DIR, 'examples/templates')
)

WSGI_APPLICATION = 'mydjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'dev',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'CHARSET': 'utf-8'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = "zh-CN"     #   "en-us"

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


import os
HAYSTACK_CONNECTIONS = {
'default': {
    'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
    'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
},
}

'''grappelli相关配置开始'''
# TEMPLATE_CONTEXT_PROCESSORS = (
#     "django.contrib.auth.context_processors.auth",
#     "django.core.context_processors.debug",
#     "django.core.context_processors.i18n",
#     "django.core.context_processors.media",
#     "django.core.context_processors.static",
#     "django.core.context_processors.tz",
#     "django.contrib.messages.context_processors.messages"
# )
#
# ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
#
#
# DEBUG_TOOLBAR_PANELS = [
#         'debug_toolbar.panels.versions.VersionsPanel',
#         'debug_toolbar.panels.timer.TimerPanel',
#         'debug_toolbar.panels.settings.SettingsPanel',
#         'debug_toolbar.panels.headers.HeadersPanel',
#         'debug_toolbar.panels.request.RequestPanel',
#         'debug_toolbar.panels.sql.SQLPanel',
#         'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#         'debug_toolbar.panels.templates.TemplatesPanel',
#         'debug_toolbar.panels.cache.CachePanel',
#         'debug_toolbar.panels.signals.SignalsPanel',
#         'debug_toolbar.panels.logging.LoggingPanel',
#         'debug_toolbar.panels.redirects.RedirectsPanel',
#     ]
# GRAPPELLI_ADMIN_TITLE = u'Django练习用的后台管理系统'
# GRAPPELLI_SWITCH_USER = True
'''grappelli相关配置结束'''

'''DEBUG_TOOLBAR 配置开始'''
DEBUG_TOOLBAR_PATCH_SETTINGS = True
INTERNAL_IPS = ('127.0.0.1', )

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'JQUERY_URL': 'http://127.0.0.1:8000/static/admin/js/jquery.js'
}
'''DEBUG_TOOLBAR 配置结束'''



'''django_admin_bootstrapped配置开始'''
DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'
from django.contrib import messages

MESSAGE_TAGS = {
            messages.SUCCESS: 'alert-success success',
            messages.WARNING: 'alert-warning warning',
            messages.ERROR: 'alert-danger error'
}
'''django_admin_bootstrapped配置结束'''