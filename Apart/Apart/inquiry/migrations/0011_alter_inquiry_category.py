# Generated by Django 3.2.4 on 2021-08-06 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0010_alter_inquiry_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inquiry.categorymodel'),
        ),
    ]
