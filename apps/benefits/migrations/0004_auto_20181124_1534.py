# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-24 05:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benefits', '0003_auto_20181117_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='benefit',
            name='content_ru',
        ),
        migrations.RemoveField(
            model_name='benefit',
            name='title_ru',
        ),
    ]
