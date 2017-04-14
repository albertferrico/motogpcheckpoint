# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('historia', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
    ]