# Generated by Django 4.2.4 on 2023-08-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_car_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
