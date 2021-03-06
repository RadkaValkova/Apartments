# Generated by Django 3.2.4 on 2021-08-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0008_alter_inquiry_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='name',
            field=models.CharField(choices=[('', 'всички'), ('покупка/продажба', 'покупка/продажба'), ('наема/отдава под наем', 'наема/отдава под наем'), ('пазарна оценка', 'пазарна оценка'), ('друго', 'друго')], max_length=30),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='category',
            field=models.CharField(choices=[('', 'всички'), ('покупка/продажба', 'покупка/продажба'), ('наема/отдава под наем', 'наема/отдава под наем'), ('пазарна оценка', 'пазарна оценка'), ('друго', 'друго')], max_length=30),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='first_name',
            field=models.CharField(max_length=15, verbose_name='Име'),
        ),
    ]
