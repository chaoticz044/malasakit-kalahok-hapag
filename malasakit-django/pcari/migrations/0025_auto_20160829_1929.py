# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-29 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0024_auto_20160829_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landing', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('review', models.IntegerField(default=0)),
                ('bloom', models.IntegerField(default=0)),
                ('peer_rating', models.IntegerField(default=0)),
                ('comment', models.IntegerField(default=0)),
                ('logout', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='userprogression',
            name='completion_rate',
            field=models.IntegerField(default=0),
        ),
    ]