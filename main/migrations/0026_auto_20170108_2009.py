# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-01-08 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20170108_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/main/articleImages'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/main/scheduleImages'),
        ),
    ]
