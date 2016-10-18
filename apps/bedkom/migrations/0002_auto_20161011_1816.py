# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bedkom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='info',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='notes',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='telephone',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='priority',
            field=models.CharField(choices=[('Høy', 'HØY'), ('Middels', 'MIDDELS'), ('Lav', 'LAV')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(choices=[('Booket', 'BOOKET'), ('Opprettet kontaktet', 'KONTAKTET'), ('Takket nei', 'NEI'), ('Ikke kontaktet', 'IKKE_KONTAKTET'), ('Sendt mail', 'SENDT_MAIL')], max_length=20),
        ),
    ]