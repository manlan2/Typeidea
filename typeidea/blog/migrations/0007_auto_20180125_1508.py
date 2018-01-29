# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-25 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pv',
            field=models.PositiveIntegerField(default=0, verbose_name='pv'),
        ),
        migrations.AddField(
            model_name='post',
            name='uv',
            field=models.PositiveIntegerField(default=0, verbose_name='uv'),
        ),
    ]
