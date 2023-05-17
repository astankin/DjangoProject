# Generated by Django 4.2.1 on 2023-05-17 12:39

import MyPlantApp.authapp.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[MyPlantApp.authapp.validators.user_name_validator])),
                ('last_name', models.CharField(max_length=20, validators=[MyPlantApp.authapp.validators.user_name_validator])),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
