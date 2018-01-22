# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-09 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugBankID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drugbank_id', models.CharField(blank=True, max_length=200, null=True)),
                ('url', models.URLField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Target',
        ),
    ]