# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilotos', '0004_auto_20161111_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='piloto',
            name='lug',
            field=models.CharField(default=b'piloto', max_length=255),
        ),
    ]
