from django.db import migrations
from django.db.models.fields.related_descriptors import (
    ForwardManyToOneDescriptor,
    ForwardOneToOneDescriptor,
    ManyToManyDescriptor,
    ReverseManyToOneDescriptor,
    ReverseOneToOneDescriptor,
)

plugin = {
    "python_module": {
        "health_check_schedule": None,
        "update_schedule": None,
        "module": "phishing.phishing_form_compiler.PhishingFormCompiler",
        "base_path": "api_app.analyzers_manager.file_analyzers",
    },
    "name": "Phishing_Form_Compiler",
    "description": "Analyzer that retrieves all forms in page and tries to compile and submit them.",
    "disabled": False,
    "soft_time_limit": 60,
    "routing_key": "default",
    "health_check_status": True,
    "type": "file",
    "docker_based": True,
    "maximum_tlp": "RED",
    "observable_supported": [],
    "supported_filetypes": [
        "application/javascript",
        "application/x-javascript",
        "text/javascript",
        "text/html",
    ],
    "run_hash": False,
    "run_hash_type": "",
    "not_supported_filetypes": [],
    "model": "analyzers_manager.AnalyzerConfig",
}

params = [
    {
        "python_module": {
            "module": "phishing.phishing_form_compiler.PhishingFormCompiler",
            "base_path": "api_app.analyzers_manager.file_analyzers",
        },
        "name": "xpath_selector",
        "type": "str",
        "description": "XPath expression to match a form on phishing page.",
        "is_secret": False,
        "required": False,
    },
    {
        "python_module": {
            "module": "phishing.phishing_form_compiler.PhishingFormCompiler",
            "base_path": "api_app.analyzers_manager.file_analyzers",
        },
        "name": "proxy_protocol",
        "type": "str",
        "description": "Protocol used for proxy connection. Can be set only if proxy_address has been set.",
        "is_secret": False,
        "required": False,
    },
    {
        "python_module": {
            "module": "phishing.phishing_form_compiler.PhishingFormCompiler",
            "base_path": "api_app.analyzers_manager.file_analyzers",
        },
        "name": "proxy_address",
        "type": "str",
        "description": "Address for proxy to use for requests.",
        "is_secret": False,
        "required": False,
    },
    {
        "python_module": {
            "module": "phishing.phishing_form_compiler.PhishingFormCompiler",
            "base_path": "api_app.analyzers_manager.file_analyzers",
        },
        "name": "proxy_port",
        "type": "int",
        "description": "Port for proxy to use for requests. Can be set only if proxy_address has been set.",
        "is_secret": False,
        "required": False,
    },
]

values = [
    {
        "parameter": {
            "python_module": {
                "module": "phishing.phishing_form_compiler.PhishingFormCompiler",
                "base_path": "api_app.analyzers_manager.file_analyzers",
            },
            "name": "xpath_selector",
            "type": "str",
            "description": "XPath expression to match a form on phishing page.",
            "is_secret": False,
            "required": False,
        },
        "analyzer_config": "Phishing_Form_Compiler",
        "connector_config": None,
        "visualizer_config": None,
        "ingestor_config": None,
        "pivot_config": None,
        "for_organization": False,
        "value": "//*[self::form or self::iframe or self::fieldset][.//input[not(@type) or @type='' or @type='text']][.//input[@type='password']][.//input[@type='submit' or contains(@class, 'submit')] or .//button[not(@type) or @type='' or @type='submit' or contains(@class, 'submit')]]",
        "updated_at": "2024-10-10T09:29:36.730485Z",
        "owner": None,
    },
    {
        "parameter": {
            "python_module": {
                "module": "phishing.phishing_form_compiler.PhishingFormCompiler",
                "base_path": "api_app.analyzers_manager.file_analyzers",
            },
            "name": "proxy_protocol",
            "type": "str",
            "description": "Protocol used for proxy connection. Can be set only if proxy_address has been set.",
            "is_secret": False,
            "required": False,
        },
        "analyzer_config": "Phishing_Form_Compiler",
        "connector_config": None,
        "visualizer_config": None,
        "ingestor_config": None,
        "pivot_config": None,
        "for_organization": False,
        "value": "",
        "updated_at": "2024-10-10T09:29:36.730485Z",
        "owner": None,
    },
    {
        "parameter": {
            "python_module": {
                "module": "phishing.phishing_form_compiler.PhishingFormCompiler",
                "base_path": "api_app.analyzers_manager.file_analyzers",
            },
            "name": "proxy_address",
            "type": "str",
            "description": "Address for proxy to use for requests.",
            "is_secret": False,
            "required": False,
        },
        "analyzer_config": "Phishing_Form_Compiler",
        "connector_config": None,
        "visualizer_config": None,
        "ingestor_config": None,
        "pivot_config": None,
        "for_organization": False,
        "value": "",
        "updated_at": "2024-10-10T09:29:36.730485Z",
        "owner": None,
    },
    {
        "parameter": {
            "python_module": {
                "module": "phishing.phishing_form_compiler.PhishingFormCompiler",
                "base_path": "api_app.analyzers_manager.file_analyzers",
            },
            "name": "proxy_port",
            "type": "int",
            "description": "Port for proxy to use for requests. Can be set only if proxy_address has been set.",
            "is_secret": False,
            "required": False,
        },
        "analyzer_config": "Phishing_Form_Compiler",
        "connector_config": None,
        "visualizer_config": None,
        "ingestor_config": None,
        "pivot_config": None,
        "for_organization": False,
        "value": 0,
        "updated_at": "2024-10-10T09:29:36.730485Z",
        "owner": None,
    },
]


def _get_real_obj(Model, field, value):
    def _get_obj(Model, other_model, value):
        if isinstance(value, dict):
            real_vals = {}
            for key, real_val in value.items():
                real_vals[key] = _get_real_obj(other_model, key, real_val)
            value = other_model.objects.get_or_create(**real_vals)[0]
        # it is just the primary key serialized
        else:
            if isinstance(value, int):
                if Model.__name__ == "PluginConfig":
                    value = other_model.objects.get(name=plugin["name"])
                else:
                    value = other_model.objects.get(pk=value)
            else:
                value = other_model.objects.get(name=value)
        return value

    if (
        type(getattr(Model, field))
        in [
            ForwardManyToOneDescriptor,
            ReverseManyToOneDescriptor,
            ReverseOneToOneDescriptor,
            ForwardOneToOneDescriptor,
        ]
        and value
    ):
        other_model = getattr(Model, field).get_queryset().model
        value = _get_obj(Model, other_model, value)
    elif type(getattr(Model, field)) in [ManyToManyDescriptor] and value:
        other_model = getattr(Model, field).rel.model
        value = [_get_obj(Model, other_model, val) for val in value]
    return value


def _create_object(Model, data):
    mtm, no_mtm = {}, {}
    for field, value in data.items():
        value = _get_real_obj(Model, field, value)
        if type(getattr(Model, field)) is ManyToManyDescriptor:
            mtm[field] = value
        else:
            no_mtm[field] = value
    try:
        o = Model.objects.get(**no_mtm)
    except Model.DoesNotExist:
        o = Model(**no_mtm)
        o.full_clean()
        o.save()
        for field, value in mtm.items():
            attribute = getattr(o, field)
            if value is not None:
                attribute.set(value)
        return False
    return True


def migrate(apps, schema_editor):
    Parameter = apps.get_model("api_app", "Parameter")
    PluginConfig = apps.get_model("api_app", "PluginConfig")
    python_path = plugin.pop("model")
    Model = apps.get_model(*python_path.split("."))
    if not Model.objects.filter(name=plugin["name"]).exists():
        exists = _create_object(Model, plugin)
        if not exists:
            for param in params:
                _create_object(Parameter, param)
            for value in values:
                _create_object(PluginConfig, value)


def reverse_migrate(apps, schema_editor):
    python_path = plugin.pop("model")
    Model = apps.get_model(*python_path.split("."))
    Model.objects.get(name=plugin["name"]).delete()


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ("api_app", "0062_alter_parameter_python_module"),
        ("analyzers_manager", "0122_alter_soft_time_limit"),
    ]

    operations = [migrations.RunPython(migrate, reverse_migrate)]