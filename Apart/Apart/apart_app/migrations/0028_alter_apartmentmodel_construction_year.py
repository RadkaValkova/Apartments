# Generated by Django 3.2.4 on 2021-07-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apart_app', '0027_alter_apartmentmodel_town'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentmodel',
            name='construction_year',
            field=models.CharField(max_length=4),
        ),
    ]