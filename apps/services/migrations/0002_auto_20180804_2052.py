# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-04 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceimage',
            name='service',
        ),
        migrations.RemoveField(
            model_name='service',
            name='logo',
        ),
        migrations.AddField(
            model_name='service',
            name='icon_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Название иконки'),
        ),
        migrations.DeleteModel(
            name='ServiceImage',
        ),
    ]
