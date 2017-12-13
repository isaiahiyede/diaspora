# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_auto_20170827_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='room_type',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
