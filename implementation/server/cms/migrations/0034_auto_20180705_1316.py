# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-05 18:16
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0033_auto_20180705_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='hero_text',
            field=wagtail.core.fields.RichTextField(),
        ),
    ]