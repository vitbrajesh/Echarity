# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import products.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                ('description', models.CharField(default=False, max_length=60)),
                ('active', models.BooleanField(default=True)),
                ('quantity', models.IntegerField(default=0)),
                ('zip_Code', models.CharField(max_length=6, blank=True)),
                ('address', models.CharField(default=False, max_length=60)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_Update', models.DateTimeField(null=True, blank=True)),
                ('expire_date', models.DateTimeField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('docfile',),
                'verbose_name': 'Product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='Product1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(null=True, blank=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('active', models.BooleanField(default=True)),
                ('quantity', models.IntegerField(default=0)),
                ('zip_Code', models.CharField(max_length=6, blank=True)),
                ('address', models.CharField(default=False, max_length=60)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_Update', models.DateTimeField(null=True, blank=True)),
                ('expire_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=products.models.image_upload_to)),
                ('order', models.IntegerField(default=0)),
                ('url_link', models.CharField(max_length=250, null=True, blank=True)),
                ('header_text', models.CharField(max_length=120, null=True, blank=True)),
                ('text', models.CharField(max_length=120, null=True, blank=True)),
                ('active', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'ordering': ['order', '-start_date', '-end_date'],
            },
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('saleprice', models.DecimalField(max_digits=10, decimal_places=2)),
                ('active', models.BooleanField(default=True)),
                ('inventory', models.IntegerField(null=True, blank=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
    ]
