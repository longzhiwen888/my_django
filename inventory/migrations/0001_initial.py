# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('goods_no', models.CharField(max_length=255, serialize=False, verbose_name='\u8d27\u7269\u7f16\u53f7', primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u8d27\u7269\u540d\u79f0')),
                ('category', models.CharField(max_length=255, verbose_name='\u8d27\u7269\u7c7b\u522b')),
                ('measurement_unit', models.CharField(max_length=255, verbose_name='\u8ba1\u91cf\u5355\u4f4d')),
            ],
            options={
                'verbose_name': '\u8d27\u7269',
                'verbose_name_plural': '\u8d27\u7269\u4fe1\u606f\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='InboundOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_no', models.CharField(max_length=255, verbose_name='\u5165\u5e93\u5355\u7f16\u53f7')),
                ('goods_no', models.CharField(max_length=255, verbose_name='\u8d27\u7269\u7f16\u53f7')),
                ('goods_num', models.IntegerField(verbose_name='\u8d27\u7269\u6570\u91cf')),
                ('warehouse_no', models.CharField(max_length=255, verbose_name='\u4ed3\u5e93\u7f16\u53f7')),
                ('goods_price', models.FloatField(verbose_name='\u8d27\u7269\u5355\u4ef7')),
                ('supplier_no', models.CharField(max_length=255, verbose_name='\u4f9b\u5e94\u5546\u7f16\u53f7')),
                ('create_time', models.DateTimeField(verbose_name='\u5165\u5e93\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5165\u5e93\u5355',
                'verbose_name_plural': '\u5165\u5e93\u5355\u4fe1\u606f\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('warehouse_no', models.CharField(max_length=255, verbose_name='\u4ed3\u5e93\u7f16\u53f7')),
                ('goods_no', models.CharField(max_length=255, verbose_name='\u8d27\u7269\u7f16\u53f7')),
                ('goods_num', models.IntegerField(verbose_name='\u5e93\u5b58\u6570\u91cf')),
            ],
            options={
                'verbose_name': '\u5e93\u5b58',
                'verbose_name_plural': '\u5e93\u5b58\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name='\u7ba1\u7406\u5458\u7f16\u53f7', primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u7ba1\u7406\u5458\u540d\u79f0')),
                ('contact_phone', models.CharField(max_length=255, verbose_name='\u7ba1\u7406\u5458\u7535\u8bdd')),
            ],
            options={
                'verbose_name': '\u7ba1\u7406\u5458',
                'verbose_name_plural': '\u7ba1\u7406\u5458\u4fe1\u606f\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='OutboundOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_no', models.CharField(max_length=255, verbose_name='\u51fa\u5e93\u5355\u7f16\u53f7')),
                ('goods_no', models.CharField(max_length=255, verbose_name='\u8d27\u7269\u7f16\u53f7')),
                ('goods_num', models.IntegerField(verbose_name='\u8d27\u7269\u6570\u91cf')),
                ('warehouse_no', models.CharField(max_length=255, verbose_name='\u4ed3\u5e93\u7f16\u53f7')),
                ('create_time', models.DateTimeField(verbose_name='\u51fa\u5e93\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u51fa\u5e93\u5355',
                'verbose_name_plural': '\u51fa\u5e93\u5355\u4fe1\u606f\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name='\u4f9b\u5e94\u5546\u7f16\u53f7', primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u4f9b\u5e94\u5546\u540d\u79f0')),
                ('contact_name', models.CharField(max_length=255, verbose_name='\u8054\u7cfb\u4eba\u540d\u79f0')),
                ('contact_phone', models.CharField(max_length=255, verbose_name='\u8054\u7cfb\u4eba\u7535\u8bdd')),
                ('address', models.CharField(max_length=255, verbose_name='\u4f9b\u5e94\u5546\u5730\u5740')),
            ],
            options={
                'verbose_name': '\u4f9b\u5e94\u5546',
                'verbose_name_plural': '\u4f9b\u5e94\u5546\u4fe1\u606f\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u4ed3\u5e93\u540d\u79f0')),
                ('address', models.CharField(max_length=255, verbose_name='\u4ed3\u5e93\u5730\u70b9')),
                ('admin_id', models.IntegerField(verbose_name='\u4ed3\u5e93\u7ba1\u7406\u4eba\u5458\u7f16\u53f7')),
            ],
            options={
                'verbose_name': '\u4ed3\u5e93',
                'verbose_name_plural': '\u4ed3\u5e93\u4fe1\u606f\u7ba1\u7406',
            },
        ),
        migrations.AlterUniqueTogether(
            name='inventory',
            unique_together=set([('warehouse_no', 'goods_no')]),
        ),
    ]
