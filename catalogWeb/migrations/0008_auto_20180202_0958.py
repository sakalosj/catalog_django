# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-02 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogWeb', '0007_auto_20180202_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='monumentList',
            field=models.ManyToManyField(blank=True, through='catalogWeb.Monument2Project', to='catalogWeb.Monument'),
        ),
    ]