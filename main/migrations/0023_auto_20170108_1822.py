# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-01-08 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20170108_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content3',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content2',
            field=models.TextField(blank=True),
        ),
    ]