# Generated by Django 3.2.4 on 2021-07-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profiles'),
        ),
    ]
