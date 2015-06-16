#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.apps import AuthConfig as _AuthConfig
from django.contrib.admin.apps import AdminConfig as _AdminConfig
from django.apps import AppConfig
from inventory import models


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


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('warehouse_no', 'goods_no', 'goods_num')
    search_fields = ('warehouse_no', 'goods_no')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        result = super(InventoryAdmin, self).change_view(
            request, object_id,
            form_url=form_url,
            extra_context=extra_context)

        document = models.Inventory.objects.get(id__exact=object_id)

        if '_addanother' not in request.POST and \
                '_continue' not in request.POST:
            result['Location'] = document.get_absolute_url()
        return result


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'admin_id')
    search_fields = ('id', 'name', 'address')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        result = super(InventoryAdmin, self).change_view(
            request, object_id,
            form_url=form_url,
            extra_context=extra_context)

        document = models.Warehouse.objects.get(id__exact=object_id)

        if '_addanother' not in request.POST and \
                '_continue' not in request.POST:
            result['Location'] = document.get_absolute_url()
        return result


admin.site.register(models.Inventory, InventoryAdmin)
admin.site.register(models.Warehouse, WarehouseAdmin)
