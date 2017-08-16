# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import shorter.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0003_auto_20170814_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shorter.validators.validate_url]),
        ),
    ]