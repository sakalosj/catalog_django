# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-19 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20180212_2104'),
        ('catalogWeb', '0002_auto_20180210_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='restorer',
            name='album',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='album.Album'),
        ),
        migrations.AlterField(
            model_name='material',
            name='album',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='album.Album'),
        ),
        migrations.AlterField(
            model_name='research',
            name='album',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='album.Album'),
        ),
    ]
