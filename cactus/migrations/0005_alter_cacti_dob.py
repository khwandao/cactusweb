# Generated by Django 3.2.4 on 2021-06-14 05:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cactus', '0004_cacti_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cacti',
            name='dob',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 14, 12, 58, 32, 767989)),
        ),
    ]
