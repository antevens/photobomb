# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                 ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                 ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                 ('heading', models.CharField(max_length=256, default='Figure 1 ....')),
                 ('footer', models.CharField(max_length=256, default='Source .....')),
            ],
        ),
    ]
