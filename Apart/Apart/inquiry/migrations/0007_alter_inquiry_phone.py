# Generated by Django 3.2.4 on 2021-07-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0006_alter_inquiry_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
