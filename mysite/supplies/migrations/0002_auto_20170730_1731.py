# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.AddField(
            model_name='item',
            name='item_quantity',
            field=models.IntegerField(blank=1, default=1),
            preserve_default=False,
        ),
    ]