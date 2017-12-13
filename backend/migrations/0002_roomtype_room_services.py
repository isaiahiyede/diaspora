# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='room_services',
            field=models.CharField(max_length=1500, null=True, blank=True),
        ),
    ]
