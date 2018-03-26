# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-24 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogWeb', '0003_auto_20180319_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='monument',
        ),
        migrations.AddField(
            model_name='research',
            name='monument',
            field=models.ManyToManyField(blank=True, to='catalogWeb.Monument'),
        ),
    ]
