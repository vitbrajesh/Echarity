# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0004_auto_20151216_0625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                ('description', models.CharField(default=False, max_length=160)),
                ('active', models.BooleanField(default=True)),
                ('duraction', models.CharField(max_length=120)),
                ('zip_Code', models.CharField(max_length=6, blank=True)),
                ('address', models.CharField(default=False, max_length=60)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_Update', models.DateTimeField(default=django.utils.timezone.now)),
                ('expire_date', models.DateTimeField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('docfile',),
                'verbose_name': 'Service',
                'verbose_name_plural': 'products',
            },
        ),
    ]
