# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiltshop', '0011_auto_20161108_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='size',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
