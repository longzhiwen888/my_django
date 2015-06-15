# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='id',
            field=models.IntegerField(serialize=False, verbose_name='\u4ed3\u5e93\u7f16\u53f7', primary_key=True),
        ),
    ]
