# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-19 18:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_mark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marksheet',
            old_name='urid',
            new_name='uid',
        ),
    ]
