# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-30 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogWeb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monument',
            name='materialList',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogWeb.MaterialList'),
        ),
    ]
