# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-01 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogWeb', '0013_monument_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='monument',
            name='placement',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
