# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-19 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_delete_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='marksheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=120)),
                ('mark', models.CharField(max_length=120)),
                ('userid', models.CharField(max_length=120)),
            ],
        ),
    ]
