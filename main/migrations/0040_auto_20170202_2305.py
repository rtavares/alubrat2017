# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-02-02 23:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_auto_20170202_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='lame',
            new_name='lname',
        ),
    ]