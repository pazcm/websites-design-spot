# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-27 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdes', '0005_auto_20191120_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webdes',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
