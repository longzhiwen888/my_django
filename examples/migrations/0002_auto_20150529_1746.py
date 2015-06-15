# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from datetime import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='create_time',
            field=models.DateTimeField(default=datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='document',
            field=models.ForeignKey(related_name='tags', to='examples.Document'),
        ),
    ]
