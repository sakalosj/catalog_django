# Generated by Django 2.2.3 on 2019-08-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogWeb', '0003_auto_20190805_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monument',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]
