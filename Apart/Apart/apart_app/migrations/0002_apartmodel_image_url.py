# Generated by Django 3.2.4 on 2021-06-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apart_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmodel',
            name='image_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
