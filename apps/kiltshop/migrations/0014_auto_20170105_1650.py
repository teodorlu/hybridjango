# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-05 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiltshop', '0013_auto_20170103_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='link',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]