# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-25 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20161125_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='link',
            field=models.CharField(blank=True, default='#', max_length=400),
        ),
    ]