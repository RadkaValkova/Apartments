# Generated by Django 3.2.4 on 2021-06-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apart_app', '0002_apartmodel_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='townmodel',
            name='name',
            field=models.CharField(choices=[('Пловдив', 'Пловдив'), ('София', 'София'), ('Варна', 'Варна')], max_length=20),
        ),
    ]