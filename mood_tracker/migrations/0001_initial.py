# Generated by Django 3.2.23 on 2023-11-22 20:41

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SupportLocations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=100)),
                ('details', models.TextField(blank=True)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('latitude', models.FloatField(max_length=200)),
                ('longitude', models.FloatField(max_length=200)),
                ('contact_number', models.FloatField(max_length=200)),
                ('contact_email', models.FloatField(max_length=200)),
            ],
        ),
    ]
