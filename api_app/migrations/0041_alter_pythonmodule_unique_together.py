# Generated by Django 4.1.10 on 2023-08-23 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api_app", "0040_alter_pythonmodule_base_path"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="pythonmodule",
            unique_together={("module", "base_path")},
        ),
    ]
