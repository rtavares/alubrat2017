# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-02-03 00:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_registration_regdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='regDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
