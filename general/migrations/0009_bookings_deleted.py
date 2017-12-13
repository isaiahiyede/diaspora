# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0008_bookings_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
