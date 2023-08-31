# Generated by Django 4.1.10 on 2023-08-22 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "connectors_manager",
            "0019_rename_connectors__python__0fb146_idx_connectors__python__f23fd8_idx_and_more",
        ),
        ("analyzers_manager", "0039_alter_analyzerconfig_python_module"),
        (
            "visualizers_manager",
            "0024_rename_visualizers_python__2c4ded_idx_visualizers_python__8b1832_idx_and_more",
        ),
        ("pivots_manager", "0003_alter_pivot_ending_job_alter_pivot_starting_job"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pivotconfig",
            name="analyzer_config",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s",
                to="analyzers_manager.analyzerconfig",
            ),
        ),
        migrations.AlterField(
            model_name="pivotconfig",
            name="connector_config",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s",
                to="connectors_manager.connectorconfig",
            ),
        ),
        migrations.AlterField(
            model_name="pivotconfig",
            name="visualizer_config",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s",
                to="visualizers_manager.visualizerconfig",
            ),
        ),
    ]
