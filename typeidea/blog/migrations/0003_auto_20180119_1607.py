# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-19 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180118_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='blog.Tag', verbose_name='标签'),
        ),
    ]
