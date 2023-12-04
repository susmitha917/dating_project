# Generated by Django 4.2.7 on 2023-11-20 01:57

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('age', models.IntegerField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('images', models.ImageField(upload_to='images/')),
                ('distance', models.FloatField()),
                ('preference_gender', models.CharField(max_length=10)),
                ('preference_age', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('hobbies', models.TextField(blank=True, null=True)),
                ('relationship_status', models.CharField(blank=True, max_length=20, null=True)),
                ('ethnicity', models.CharField(blank=True, max_length=50, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]