# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_type', models.CharField(max_length=30, null=True, blank=True)),
                ('room_description', models.CharField(max_length=30, null=True, blank=True)),
                ('room_image', models.ImageField(null=True, upload_to=b'room_type', blank=True)),
                ('room_price_1', models.FloatField(default=0, max_length=50)),
                ('room_price_2', models.FloatField(default=0, max_length=50)),
            ],
            options={
                'verbose_name_plural': 'RoomType',
            },
        ),
    ]
