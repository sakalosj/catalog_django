# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-01 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogWeb', '0008_auto_20180326_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='CT_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='research',
            name='CT_description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
