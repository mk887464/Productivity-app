# Generated by Django 4.0.3 on 2022-06-05 22:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0007_alter_data_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date',
            field=models.DateField(default=django.utils.timezone.localtime, unique=True),
        ),
    ]