# Generated by Django 4.1.10 on 2023-08-22 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("analyzers_manager", "0037_opencti_description"),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="analyzerconfig",
            new_name="analyzers_m_python__657cda_idx",
            old_name="analyzers_m_python__3e6166_idx",
        ),
    ]
