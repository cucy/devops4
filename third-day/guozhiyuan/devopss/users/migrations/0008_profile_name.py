# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-08 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
