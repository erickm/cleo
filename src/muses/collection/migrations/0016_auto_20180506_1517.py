# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-06 20:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muses_collection', '0015_auto_20180506_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='period_start_en',
            new_name='object_date_begin_en',
        ),
    ]
