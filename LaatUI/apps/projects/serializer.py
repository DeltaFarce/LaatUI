from projects.models import ProjectModel
from rest_framework.serializers import ModelSerializer
from cases.serializer import CaseModelSerializer
from reports.serializer import ReportSerializer


class ProjectModeSerializer(ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'
        read_only_fields = ['id', 'create_time', 'update_time']


class ProjectListModelSerializer(ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = ('id', 'name')


class ProjectToTestCaseModelSerializer(ModelSerializer):
    case = CaseModelSerializer(many=True)

    class Meta:
        model = ProjectModel
        fields = ('id', 'case')


class ProjectToReportsModelSerializer(ModelSerializer):
    report = ReportSerializer(many=True)

    class Meta:
        model = ProjectModel
        fields = ('id', 'report')