# Generated by Django 4.2.7 on 2023-12-22 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_loggineduser_user_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggineduser',
            name='user_query',
            field=models.TextField(),
        ),
    ]
