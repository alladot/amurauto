# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-24 05:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20181117_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='content_ru',
        ),
        migrations.RemoveField(
            model_name='review',
            name='title_ru',
        ),
    ]
