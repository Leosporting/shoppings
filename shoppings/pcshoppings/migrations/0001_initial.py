# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('member_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='shopping_cpu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('item_title', models.CharField(max_length=20)),
                ('item_description', models.TextField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('item_photo', models.URLField(blank=True)),
                ('item_price', models.PositiveIntegerField(default=0)),
                ('item_location', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
