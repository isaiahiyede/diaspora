# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_roomnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomnumber',
            name='room_number',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
