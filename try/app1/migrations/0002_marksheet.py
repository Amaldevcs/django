# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-19 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='marksheet',
            fields=[
                ('fullname', models.CharField(max_length=120)),
                ('mark', models.CharField(max_length=120)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
