# Generated by Django 4.2.7 on 2023-11-22 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating_app', '0003_rename_height_userprofile_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='height',
            field=models.FloatField(),
            preserve_default=False,
        ),
    ]
