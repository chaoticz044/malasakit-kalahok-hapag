# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='progression',
            name='num_rated',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.IntegerField(default=-2),
        ),
    ]