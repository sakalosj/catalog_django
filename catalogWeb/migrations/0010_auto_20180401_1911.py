# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-01 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogWeb', '0009_auto_20180401_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='CT_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
