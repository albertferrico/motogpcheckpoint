# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-16 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_auto_20171114_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
