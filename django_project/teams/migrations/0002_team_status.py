# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-03-22 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='status',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
