# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_system', '0009_studentcomplain_complaint_finish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcomplain',
            name='complaint_finish',
            field=models.DateField(default=None),
        ),
    ]
