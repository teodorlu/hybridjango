# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-29 10:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bedkom', '0003_bedpress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='earlierbedpresses',
            name='company',
        ),
        migrations.AddField(
            model_name='bedpress',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bedkom.Company'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_person',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bedkom.Contact_person'),
        ),
        migrations.DeleteModel(
            name='EarlierBedpresses',
        ),
    ]
