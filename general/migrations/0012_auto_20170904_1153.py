# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0011_auto_20170904_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='room_number',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
