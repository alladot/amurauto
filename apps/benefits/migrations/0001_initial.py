# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-05 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название преимущества')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='Название преимущества')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='Название преимущества')),
                ('content', models.TextField(max_length=300, verbose_name='Описание')),
                ('content_ru', models.TextField(max_length=300, null=True, verbose_name='Описание')),
                ('content_en', models.TextField(max_length=300, null=True, verbose_name='Описание')),
                ('icon_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Название иконки')),
            ],
            options={
                'verbose_name': 'Преимущество',
                'verbose_name_plural': 'Преимущества',
                'ordering': ('-title',),
            },
        ),
    ]
