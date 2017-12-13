# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20170811_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='room_count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
