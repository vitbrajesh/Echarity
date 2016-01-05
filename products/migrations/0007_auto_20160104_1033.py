# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20160104_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='docfile',
            field=models.FileField(default=datetime.datetime(2016, 1, 4, 10, 33, 49, 502565, tzinfo=utc), upload_to=b'documents/%Y/%m/%d', blank=True),
            preserve_default=False,
        ),
    ]
