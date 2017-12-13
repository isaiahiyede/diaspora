# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_bookings_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='room_number',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
    ]
