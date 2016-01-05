# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='docfile',
            field=models.FileField(null=True, upload_to=b'documents/%Y/%m/%d', blank=True),
        ),
    ]
