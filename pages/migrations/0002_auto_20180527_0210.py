# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-27 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='header_title',
            field=models.CharField(max_length=100),
        ),
    ]