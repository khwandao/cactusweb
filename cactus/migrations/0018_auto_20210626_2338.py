# Generated by Django 3.2.4 on 2021-06-26 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cactus', '0017_auto_20210626_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cacti',
            name='dob',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 26, 23, 38, 29, 323416)),
        ),
        migrations.AlterModelTable(
            name='colortype',
            table='cactus_color_type',
        ),
    ]
