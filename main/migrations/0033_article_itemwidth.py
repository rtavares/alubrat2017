# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-01-15 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20170112_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='itemWidth',
            field=models.IntegerField(default=3, verbose_name='itemWidth 12, 6, 3'),
        ),
    ]