# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-22 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_remove_transaction_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_info',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='finance.TransactionInfo'),
            preserve_default=False,
        ),
    ]
