# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0013_auto_20160804_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quantitative_Question',
            fields=[
                ('qid', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(default='', max_length=500)),
                ('tagalog_question', models.CharField(default='walang tagalog pagsasalin', max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
