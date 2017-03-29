# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-02-02 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20170202_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='cell',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='registration',
            name='f2address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='f2cell',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='registration',
            name='f2city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='f2country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='f2email',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='registration',
            name='f2fname',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='registration',
            name='f2nif',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='f2phone',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='registration',
            name='f2zip',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]