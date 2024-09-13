# Generated by Django 4.2.11 on 2024-05-07 13:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0005_create_profiles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="company_name",
            field=models.CharField(
                blank=True,
                default="",
                max_length=32,
                validators=[django.core.validators.MinLengthValidator(3)],
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="company_role",
            field=models.CharField(
                blank=True,
                default="",
                max_length=32,
                validators=[django.core.validators.MinLengthValidator(3)],
            ),
        ),
    ]
