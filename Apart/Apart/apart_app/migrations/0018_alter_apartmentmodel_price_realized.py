# Generated by Django 3.2.4 on 2021-07-15 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apart_app', '0017_alter_apartmentmodel_town'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentmodel',
            name='price_realized',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
