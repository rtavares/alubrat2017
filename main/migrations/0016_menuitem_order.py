# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-01-06 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20170106_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
