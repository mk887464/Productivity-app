# Generated by Django 4.0.3 on 2022-05-13 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0003_data_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='user',
        ),
    ]
