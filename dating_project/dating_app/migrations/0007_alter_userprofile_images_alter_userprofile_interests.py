# Generated by Django 4.2.7 on 2023-12-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating_app', '0006_alter_userprofile_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='interests',
            field=models.CharField(max_length=255),
        ),
    ]
