# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0012_auto_20170904_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='new_booking',
            field=models.BooleanField(default=True),
        ),
    ]
