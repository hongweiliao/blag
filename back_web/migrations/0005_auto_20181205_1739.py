# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back_web', '0004_auto_20181204_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='back_web.Item'),
        ),
    ]