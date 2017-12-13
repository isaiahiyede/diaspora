# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_auto_20170827_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='checK_in',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bookings',
            name='checK_out',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
