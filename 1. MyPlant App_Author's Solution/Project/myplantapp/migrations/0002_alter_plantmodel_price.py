# Generated by Django 4.2.1 on 2023-05-18 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myplantapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantmodel',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
    ]
