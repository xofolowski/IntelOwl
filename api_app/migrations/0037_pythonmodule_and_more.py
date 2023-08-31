# Generated by Django 4.1.10 on 2023-08-22 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("connectors_manager", "0018_alter_connectorconfig_name"),
        ("visualizers_manager", "0023_alter_visualizerconfig_name"),
        ("ingestors_manager", "0004_alter_ingestorreport_name"),
        (
            "analyzers_manager",
            "0038_rename_analyzers_m_python__3e6166_idx_analyzers_m_python__657cda_idx",
        ),
        ("api_app", "0036_alter_parameter_unique_together_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PythonModule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("module", models.CharField(db_index=True, max_length=120)),
                ("base_path", models.CharField(db_index=True, max_length=120)),
            ],
        ),
        migrations.RemoveIndex(
            model_name="parameter",
            name="api_app_par_analyze_1f1bee_idx",
        ),
        migrations.RemoveIndex(
            model_name="parameter",
            name="api_app_par_connect_a49bf6_idx",
        ),
        migrations.RemoveIndex(
            model_name="parameter",
            name="api_app_par_visuali_99f678_idx",
        ),
        migrations.RemoveIndex(
            model_name="parameter",
            name="api_app_par_ingesto_517684_idx",
        ),
        migrations.AddField(
            model_name="pluginconfig",
            name="analyzer_config",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s",
                to="analyzers_manager.analyzerconfig",
            ),
        ),
        migrations.AddField(
            model_name="pluginconfig",
            name="connector_config",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s",
                to="connectors_manager.connectorconfig",
            ),
        ),
        migrations.AddField(
            model_name="pluginconfig",
            name="ingestor_config",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s",
                to="ingestors_manager.ingestorconfig",
            ),
        ),
        migrations.AddField(
            model_name="pluginconfig",
            name="visualizer_config",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s",
                to="visualizers_manager.visualizerconfig",
            ),
        ),
        migrations.AlterField(
            model_name="parameter",
            name="is_secret",
            field=models.BooleanField(db_index=True),
        ),
        migrations.AddIndex(
            model_name="pluginconfig",
            index=models.Index(
                fields=["ingestor_config"], name="api_app_plu_ingesto_d7a20e_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="pluginconfig",
            index=models.Index(
                fields=["analyzer_config"], name="api_app_plu_analyze_e62bf2_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="pluginconfig",
            index=models.Index(
                fields=["connector_config"], name="api_app_plu_connect_da4207_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="pluginconfig",
            index=models.Index(
                fields=["visualizer_config"], name="api_app_plu_visuali_54319e_idx"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="parameter",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="parameter",
            name="python_module",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="parameters",
                to="api_app.pythonmodule",
                null=True,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="parameter",
            unique_together={("name", "python_module")},
        ),
    ]
