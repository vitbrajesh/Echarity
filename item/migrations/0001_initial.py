# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donatable_item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('quantity', models.IntegerField()),
                ('slug', models.SlugField(max_length=150)),
                ('photo', models.ImageField(upload_to=b'images', blank=True)),
                ('zip_Code', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_Update', models.DateTimeField(null=True, blank=True)),
                ('expire_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
