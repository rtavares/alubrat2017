# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-02-02 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20170202_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='cell',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
