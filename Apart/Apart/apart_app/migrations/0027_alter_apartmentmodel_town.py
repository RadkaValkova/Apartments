# Generated by Django 3.2.4 on 2021-07-25 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apart_app', '0026_auto_20210725_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentmodel',
            name='town',
            field=models.CharField(max_length=30),
        ),
    ]
