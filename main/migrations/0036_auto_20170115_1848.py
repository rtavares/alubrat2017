# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-01-15 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20170115_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='itemWidth',
            field=models.IntegerField(default=3, null=True, verbose_name='itemWidth - (12, 6, 3)'),
        ),
    ]