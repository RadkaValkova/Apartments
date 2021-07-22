# Generated by Django 3.2.4 on 2021-06-26 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apart_app', '0005_auto_20210622_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('family_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
