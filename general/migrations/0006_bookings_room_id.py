# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_bookings_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='room_id',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
