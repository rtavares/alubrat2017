# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-01-08 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20170108_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content2',
            field=models.CharField(max_length=800),
        ),
    ]
