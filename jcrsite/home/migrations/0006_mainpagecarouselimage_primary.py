# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170317_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpagecarouselimage',
            name='primary',
            field=models.BooleanField(default=False),
        ),
    ]
