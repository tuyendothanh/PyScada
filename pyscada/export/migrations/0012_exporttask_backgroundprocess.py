# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-07 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0038_auto_20170707_1209'),
        ('export', '0011_exporttask_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='exporttask',
            name='backgroundprocess',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyscada.BackgroundProcess'),
        ),
    ]