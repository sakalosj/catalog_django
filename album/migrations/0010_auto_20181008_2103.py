# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-08 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0009_auto_20181008_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='image2',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
