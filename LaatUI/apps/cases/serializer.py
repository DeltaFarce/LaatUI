from rest_framework.serializers import ModelSerializer
from cases.models import CaseModel
from reports.models import ReportModel


class CaseToStateModelSerializer(ModelSerializer):
    class Meta:
        model = ReportModel
        fields = ['state']
        read_only_fields = ['state']


class CaseToReportModelSerializer(ModelSerializer):
    case = CaseToStateModelSerializer(many=True)

    class Meta:
        model = CaseModel
        fields = '__all__'
        read_only_fields = ['id', 'create_time', 'update_time', 'case']


class CaseModelSerializer(ModelSerializer):
    # case = CaseToStateModelSerializer(many=True)

    class Meta:
        model = CaseModel
        fields = '__all__'
        read_only_fields = ['id', 'create_time', 'update_time']




