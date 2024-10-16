from rest_flex_fields import FlexFieldsModelSerializer

from api_app.data_model_manager.models import (
    DomainDataModel,
    FileDataModel,
    IETFReport,
    IPDataModel,
    Signature,
)


class IETFReportSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = IETFReport
        fields = "__all__"


class SignatureSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Signature
        fields = "__all__"


class DomainDataModelSerializer(FlexFieldsModelSerializer):
    ietf_report = IETFReportSerializer()

    class Meta:
        model = DomainDataModel
        fields = "__all__"


class IPDataModelSerializer(FlexFieldsModelSerializer):
    ietf_report = IETFReportSerializer()

    class Meta:
        model = IPDataModel
        fields = "__all__"


class FileDataModelSerializer(FlexFieldsModelSerializer):
    signatures = SignatureSerializer(many=True)

    class Meta:
        model = FileDataModel
        fields = "__all__"
