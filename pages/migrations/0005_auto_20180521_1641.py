# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-21 16:41
from __future__ import unicode_literals

from django.db import migrations
import tinymce_4.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20180521_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='body_heading',
            field=tinymce_4.fields.TinyMCEModelField(blank=True, null=True, verbose_name='TinyMCEModelField'),
        ),
    ]
