from reports.models import ReportModel
from rest_framework.serializers import ModelSerializer


class ReportSerializer(ModelSerializer):
    class Meta:
        model = ReportModel
        fields = '__all__'
        read_only_fields = ['id', 'create_time', 'state']

