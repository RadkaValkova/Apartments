# Generated by Django 3.2.4 on 2021-07-20 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apart_app', '0022_alter_apartmentmodel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentmodel',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apart_app.typemodel'),
        ),
    ]