# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_bookings_room_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='amount_paid',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
