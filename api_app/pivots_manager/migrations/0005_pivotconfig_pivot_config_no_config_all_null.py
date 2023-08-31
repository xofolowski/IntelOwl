# Generated by Django 4.1.10 on 2023-08-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pivots_manager", "0004_alter_pivotconfig_analyzer_config_and_more"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="pivotconfig",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("analyzer_config__isnull", True),
                    ("connector_config__isnull", True),
                    ("visualizer_config__isnull", True),
                    _connector="OR",
                ),
                name="pivot_config_no_config_all_null",
            ),
        ),
    ]
