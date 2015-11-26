# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0002_auto_20151110_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='List_items1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('quentity', models.IntegerField()),
                ('zipcode', models.CharField(max_length=6)),
                ('discription', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(null=True, blank=True)),
                ('expiry_date', models.DateTimeField(null=True, blank=True)),
                ('address', models.CharField(max_length=200)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='list_items',
            name='author',
        ),
        migrations.DeleteModel(
            name='List_items',
        ),
    ]
