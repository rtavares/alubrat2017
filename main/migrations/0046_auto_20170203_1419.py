# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-02-03 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_auto_20170203_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='modPag',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='registration',
            name='modalidade',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
