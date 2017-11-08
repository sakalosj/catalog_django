# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-17 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogWeb', '0004_project_objects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='object_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='restorer',
            name='restorer_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
