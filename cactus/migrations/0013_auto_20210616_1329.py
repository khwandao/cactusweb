# Generated by Django 3.0.8 on 2021-06-16 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cactus', '0012_auto_20210616_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cacti',
            name='dob',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 16, 13, 29, 27, 211686)),
        ),
    ]
