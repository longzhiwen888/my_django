#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.apps import AuthConfig as _AuthConfig
from django.contrib.admin.apps import AdminConfig as _AdminConfig
from django.apps import AppConfig

from inventory import models
from django.db.models import Model


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


def init_vars_decorator(cls):
    cls.init_vars()
    return cls


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

    def __init__(self, model, admin_site):
        super(BaseModel, self).__init__(model, admin_site)
        self.init_vars()

    @classmethod
    def init_vars(cls):
        model_name = cls.__name__.replace('Admin', '')
        cls.model_obj = getattr(models, model_name)
        cls.list_display = [_.name for _ in
                            cls.model_obj._meta.fields]
        cls.search_fields = cls.list_display


@init_vars_decorator
class InventoryAdmin(BaseModel):
    pass


@init_vars_decorator
class WarehouseAdmin(BaseModel):
    pass


@init_vars_decorator
class GoodsAdmin(BaseModel):
    pass


@init_vars_decorator
class SupplierAdmin(BaseModel):
    pass

@init_vars_decorator
class ManagerAdmin(BaseModel):
    pass

@init_vars_decorator
class OutboundOrderAdmin(BaseModel):
    pass

@init_vars_decorator
class InboundOrderAdmin(BaseModel):
    pass

admin.site.register(models.Inventory, InventoryAdmin)
admin.site.register(models.Warehouse, WarehouseAdmin)
admin.site.register(models.Goods, GoodsAdmin)
admin.site.register(models.Supplier, SupplierAdmin)
admin.site.register(models.Manager, ManagerAdmin)
admin.site.register(models.OutboundOrder, OutboundOrderAdmin)
admin.site.register(models.InboundOrder, InboundOrderAdmin)

for model_name, model_class in models.__dict__.items():
    pass
