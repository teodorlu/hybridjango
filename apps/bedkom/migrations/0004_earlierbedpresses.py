# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bedkom', '0003_auto_20161011_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='EarlierBedpresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
    ]
