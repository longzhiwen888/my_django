#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class Inventory(models.Model):
    warehouse_no = models.CharField(u'仓库编号', max_length=255)
    goods_no = models.CharField(u'货物编号', max_length=255)
    goods_num = models.IntegerField(u'库存数量')

    class Meta:
        unique_together = ('warehouse_no', 'goods_no')
        verbose_name = '库存'
        verbose_name_plural = '库存管理'
        app_label = 'inventory'

    primary = ('warehouse_no', 'goods_no')

    def __unicode__(self):
        return '%s,%s' % (self.warehouse_no, self.goods_no)

    def get_absolute_url(self):
        pass


class Warehouse(models.Model):
    id = models.IntegerField(u'仓库编号', primary_key=True)  # primary_key=True
    name = models.CharField(u'仓库名称', max_length=255)
    address = models.CharField(u'仓库地点', max_length=255)
    admin_id = models.IntegerField(u'仓库管理人员编号')

    class Meta:
        verbose_name = '仓库'
        verbose_name_plural = '仓库信息管理'
        app_label = 'inventory'

    def __unicode__(self):
        return '%s' % self.id

    def get_absolute_url(self):
        pass


class Goods(models.Model):
    goods_no = models.CharField(u'货物编号', primary_key=True, max_length=255)  # primary_key=True
    name = models.CharField(u'货物名称', max_length=255)
    category = models.CharField(u'货物类别', max_length=255)
    measurement_unit = models.CharField(u'计量单位', max_length=255)

    class Meta:
        verbose_name = '货物'
        verbose_name_plural = '货物信息管理'
        app_label = 'inventory'

    def __unicode__(self):
        return '%s' % self.goods_no

    def get_absolute_url(self):
        pass


class Supplier(models.Model):
    id = models.IntegerField(u'供应商编号', primary_key=True)  # primary_key=True
    name = models.CharField(u'供应商名称', max_length=255)
    contact_name = models.CharField(u'联系人名称', max_length=255)
    contact_phone = models.CharField(u'联系人电话', max_length=255)
    address = models.CharField(u'供应商地址', max_length=255)

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = '供应商信息管理'
        app_label = 'inventory'

    def __unicode__(self):
        return '%s' % self.id

    def get_absolute_url(self):
        pass


class Manager(models.Model):
    id = models.IntegerField(u'管理员编号', primary_key=True)  # primary_key=True
    name = models.CharField(u'管理员名称', max_length=255)
    contact_phone = models.CharField(u'管理员电话', max_length=255)

    class Meta:
        verbose_name = '管理员'
        verbose_name_plural = '管理员信息管理'
        app_label = 'inventory'

    def __unicode__(self):
        return '%s' % self.id

    def get_absolute_url(self):
        pass


class OutboundOrder(models.Model):
    order_no = models.CharField(u'出库单编号', max_length=255)  # primary_key=True
    goods_no = models.CharField(u'货物编号', max_length=255)
    goods_num = models.IntegerField(u'货物数量')
    warehouse_no = models.CharField(u'仓库编号', max_length=255)
    create_time = models.DateTimeField(u'出库时间')

    class Meta:
        verbose_name = '出库单'
        verbose_name_plural = '出库单信息管理'
        app_label = 'inventory'

    def __unicode__(self):
        return '%s' % self.id

    def get_absolute_url(self):
        pass


class InboundOrder(models.Model):
    order_no = models.CharField(u'入库单编号', max_length=255)  # primary_key=True
    goods_no = models.CharField(u'货物编号', max_length=255)
    goods_num = models.IntegerField(u'货物数量')
    warehouse_no = models.CharField(u'仓库编号', max_length=255)
    goods_price = models.FloatField(u'货物单价')
    supplier_no = models.CharField(u'供应商编号', max_length=255)
    create_time = models.DateTimeField(u'入库时间')

    class Meta:
        verbose_name = '入库单'
        verbose_name_plural = '入库单信息管理'
        app_label = 'inventory'

    def __unicode__(self):
        return '%s' % self.id

    def get_absolute_url(self):
        pass
