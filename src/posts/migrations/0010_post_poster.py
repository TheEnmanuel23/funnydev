# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-05 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_remove_post_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='post_resources/'),
        ),
    ]