# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_roomtype_room_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_number', models.CharField(max_length=3, null=True, blank=True)),
                ('booked', models.BooleanField(default=False)),
                ('room_type', models.ForeignKey(blank=True, to='backend.RoomType', null=True)),
            ],
            options={
                'verbose_name_plural': 'RoomNumber',
            },
        ),
    ]
