# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-13 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muses_collection', '0034_auto_20180613_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='primary',
            field=models.BooleanField(default=False, verbose_name='Primary image'),
        ),
    ]
