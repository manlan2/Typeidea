# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-21 13:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180119_1607'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
    ]
