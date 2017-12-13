# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_roomtype_room_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomtype',
            old_name='room_services',
            new_name='room_service_others',
        ),
        migrations.RemoveField(
            model_name='roomtype',
            name='room_price_2',
        ),
        migrations.AddField(
            model_name='roomtype',
            name='days_of_week',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='room_service1',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='room_service2',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='room_service3',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='room_service4',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
