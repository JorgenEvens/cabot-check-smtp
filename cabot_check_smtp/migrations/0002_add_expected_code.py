# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-13 11:44
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('cabot_check_smtp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='SmptStatusCheck',
            name='expected_code',
            field=models.PositiveIntegerField(help_text=b'Expected response code from server', null=True, default=250),
            preserve_default=True,
        ),
    ]