# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-01-06 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20170106_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='content1',
        ),
        migrations.AddField(
            model_name='article',
            name='content2',
            field=models.CharField(default=' ', max_length=800),
            preserve_default=False,
        ),
    ]
