# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-03 14:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0026_auto_20180702_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='dutch_link',
        ),
    ]
