# Generated by Django 4.0.3 on 2022-04-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_auto_20220401_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping_List_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('bought', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=40)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
