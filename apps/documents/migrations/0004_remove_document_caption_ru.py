# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-24 05:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_remove_document_caption_en'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='caption_ru',
        ),
    ]
