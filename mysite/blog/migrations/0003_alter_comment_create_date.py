# Generated by Django 3.2.5 on 2022-05-16 06:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220516_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 16, 6, 47, 13, 328077, tzinfo=utc)),
        ),
    ]
