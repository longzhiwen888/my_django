#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.apps import AuthConfig as _AuthConfig
from django.contrib.admin.apps import AdminConfig as _AdminConfig
from django.apps import AppConfig

from inventory import models
from django.db.models import Model as DbModel


class AuthConfig(_AuthConfig):
    name = 'django.contrib.auth'
    verbose_name = u'后台用户管理'


class AdminConfig(_AdminConfig):
    name = 'django.contrib.admin'
    verbose_name = u'后台管理'


class InventoryConfig(AppConfig):
    name = u'inventory'
    verbose_name = u"库存模块管理"


class InventoryInline(admin.TabularInline):
    model = models.Inventory


class BaseModel(admin.ModelAdmin):
    list_display = None
    search_fields = None
    model_obj = None

    def change_view(self, request, object_id, form_url='', extra_context=None):
        result = super(self.__class__, self).change_view(
            request, object_id,
            form_url=form_url,
            extra_context=extra_context)

        document = models.Inventory.objects.get(id__exact=object_id)

        if '_addanother' not in request.POST and \
                '_continue' not in request.POST:
            result['Location'] = document.get_absolute_url()
        return result

    @classmethod
    def create_sub_class(cls, model_class):
        admin_class_name = model_class.__name__ + 'Admin'
        exec 'class %s(BaseModel): pass' % admin_class_name
        sub_class = locals().get(admin_class_name)
        sub_class.init_vars(model_class)
        return sub_class

    @classmethod
    def init_vars(cls, model_class):
        cls.list_display = [_.name for _ in
                            model_class._meta.fields]
        cls.search_fields = cls.list_display

for model_name, model_class in models.__dict__.items():
    try:
        if issubclass(model_class, DbModel):
            sub_class = BaseModel.create_sub_class(model_class)
            admin.site.register(model_class, sub_class)
    except:
        pass
