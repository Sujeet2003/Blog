# Generated by Django 4.2.7 on 2023-12-24 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_reviewus'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewus',
            name='testinomial_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 12, 24, 15, 50, 2, 572676, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
