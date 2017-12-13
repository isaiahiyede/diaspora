# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_remove_useraccount_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 27, 8, 57, 17, 431214, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
