# Generated by Django 3.2.4 on 2021-06-15 05:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cactus', '0008_auto_20210614_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cacti',
            name='dob',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 15, 12, 37, 16, 744793)),
        ),
    ]