# Generated by Django 4.2.4 on 2023-08-15 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_car_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='slug',
        ),
    ]
