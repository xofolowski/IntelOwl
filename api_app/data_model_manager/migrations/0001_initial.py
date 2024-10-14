# Generated by Django 4.2.15 on 2024-10-14 07:24

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analyzers_manager', '0123_analyzerconfig_mapping_data_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.CharField(max_length=100, null=True)),
                ('external_references', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), blank=True, default=list, size=None)),
                ('related_threats', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None)),
                ('malware_family', models.CharField(max_length=100, null=True)),
                ('additional_info', models.JSONField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('analyzer_report', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='data_model', to='analyzers_manager.analyzerreport')),
            ],
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=100)),
                ('signature', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='IETFReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rrname', models.CharField(max_length=100)),
                ('rrtype', models.CharField(max_length=100)),
                ('rdata', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('time_first', models.DateTimeField()),
                ('time_last', models.DateTimeField()),
            ],
            options={
                'unique_together': {('rrname', 'rrtype', 'rdata')},
            },
        ),
        migrations.CreateModel(
            name='IPDataModel',
            fields=[
                ('basedatamodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data_model_manager.basedatamodel')),
                ('asn', models.IntegerField(null=True)),
                ('asn_rank', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('certificates', models.JSONField(null=True)),
                ('org_name', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('country_code', models.CharField(max_length=100, null=True)),
                ('registered_country', models.CharField(max_length=100, null=True)),
                ('registered_country_code', models.CharField(max_length=100, null=True)),
                ('isp', models.CharField(max_length=100, null=True)),
                ('ietf_report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_model_manager.ietfreport')),
            ],
            bases=('data_model_manager.basedatamodel',),
        ),
        migrations.CreateModel(
            name='FileDataModel',
            fields=[
                ('basedatamodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data_model_manager.basedatamodel')),
                ('comments', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None)),
                ('file_information', models.JSONField(null=True)),
                ('stats', models.JSONField(null=True)),
                ('signatures', models.ManyToManyField(to='data_model_manager.signature')),
            ],
            bases=('data_model_manager.basedatamodel',),
        ),
        migrations.CreateModel(
            name='DomainDataModel',
            fields=[
                ('basedatamodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data_model_manager.basedatamodel')),
                ('rank', models.IntegerField(null=True)),
                ('ietf_report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_model_manager.ietfreport')),
            ],
            bases=('data_model_manager.basedatamodel',),
        ),
    ]
