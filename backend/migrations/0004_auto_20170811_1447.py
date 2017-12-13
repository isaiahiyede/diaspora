# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20170811_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomtype',
            name='room_description',
            field=models.CharField(max_length=1500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='room_type',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
