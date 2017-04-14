# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('circuitos', '0008_auto_20161111_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='circuito',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]