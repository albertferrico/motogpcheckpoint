# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilotos', '0002_auto_20161030_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='piloto',
            name='numero_dorsal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='piloto',
            name='perfil_piloto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
