# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0010_bookings_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='room_number',
            field=models.OneToOneField(null=True, blank=True, to='backend.RoomNumber'),
        ),
    ]
