# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-01-05 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170105_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='menuItemMouseOver',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
