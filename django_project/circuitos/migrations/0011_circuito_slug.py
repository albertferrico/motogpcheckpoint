# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('circuitos', '0010_remove_circuito_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='circuito',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
