# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_bookings_amount_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
