# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 16:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20170612_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_amount',
            new_name='total_price',
        ),
    ]