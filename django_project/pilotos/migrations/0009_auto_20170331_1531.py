# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-31 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pilotos', '0008_auto_20170331_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piloto',
            name='equipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='equipos.Equipo'),
        ),
    ]
