# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-02 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0005_remove_equipo_imagen_equipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='imagen_equipo',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
