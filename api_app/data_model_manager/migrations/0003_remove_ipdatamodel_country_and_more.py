# Generated by Django 4.2.15 on 2024-10-16 11:46

import django.contrib.postgres.fields
from django.db import migrations, models

import api_app.data_model_manager.fields


class Migration(migrations.Migration):

    dependencies = [
        ('data_model_manager', '0002_alter_basedatamodel_additional_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipdatamodel',
            name='country',
        ),
        migrations.RemoveField(
            model_name='ipdatamodel',
            name='registered_country',
        ),
        migrations.AddField(
            model_name='ipdatamodel',
            name='resolutions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), default=list, size=None),
        ),
        migrations.AddField(
            model_name='signature',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='signature',
            name='url',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='basedatamodel',
            name='evaluation',
            field=api_app.data_model_manager.fields.LowercaseCharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='basedatamodel',
            name='malware_family',
            field=api_app.data_model_manager.fields.LowercaseCharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='basedatamodel',
            name='related_threats',
            field=django.contrib.postgres.fields.ArrayField(base_field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='basedatamodel',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100), blank=True, default=None, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='filedatamodel',
            name='comments',
            field=django.contrib.postgres.fields.ArrayField(base_field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='ietfreport',
            name='rdata',
            field=django.contrib.postgres.fields.ArrayField(base_field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100), size=None),
        ),
        migrations.AlterField(
            model_name='ietfreport',
            name='rrname',
            field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ietfreport',
            name='rrtype',
            field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ipdatamodel',
            name='country_code',
            field=api_app.data_model_manager.fields.LowercaseCharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ipdatamodel',
            name='isp',
            field=api_app.data_model_manager.fields.LowercaseCharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ipdatamodel',
            name='org_name',
            field=api_app.data_model_manager.fields.LowercaseCharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ipdatamodel',
            name='registered_country_code',
            field=api_app.data_model_manager.fields.LowercaseCharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='signature',
            name='provider',
            field=api_app.data_model_manager.fields.LowercaseCharField(max_length=100),
        ),
    ]
