# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 18:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobannouncements', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='Company',
            new_name='company',
        ),
        migrations.AddField(
            model_name='job',
            name='author',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='job',
            name='logo',
            field=models.ImageField(default='placeholder-event.png', upload_to='companies'),
        ),
    ]
