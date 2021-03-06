# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiltshop', '0002_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('kiltshop_start', models.DateTimeField(blank=True, null=True)),
                ('kiltshop_end', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='order_list',
            name='orders',
            field=models.ManyToManyField(to='kiltshop.Order'),
        ),
    ]
