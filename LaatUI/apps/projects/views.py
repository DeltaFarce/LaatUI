from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from projects.models import ProjectModel
from projects.serializer import ProjectModeSerializer
from projects.serializer import ProjectListModelSerializer
from projects.serializer import ProjectToTestCaseModelSerializer
from projects.serializer import ProjectToReportsModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters


class LargeResultsSetPagination(PageNumberPagination):
    """ 自定义分页 """
    page_size = 10  # 默认每页显示多少条数据
    max_page_size = 50  # 前端在控制每页显示多少条数据时，最多不能超过5
    page_query_param = 'page'  # 前端在查询字符串的关键字时，指定显示第几页的名字，不指定默认就是page
    page_size_query_param = 'page_size'  # 前端查询字符串的关键字名字，是用来控制每页显示多少条关键字


class ProjectsViewSet(ModelViewSet):
    queryset = ProjectModel.objects.filter(is_delete=False)
    serializer_class = ProjectModeSerializer

    # 过滤、排序
    filter_backends = [DjangoFilterBackend, OrderingFilter, filters.SearchFilter]
    # 指定过滤、排序的字段
    filterset_fields = ['id', 'create_time']
    # 指定搜索字段
    search_fields = ['$name']

    # 指定分页类
    pagination_class = LargeResultsSetPagination

    @action(methods=['get'], detail=False)
    def projectList(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = ProjectListModelSerializer(qs, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def projects_cases(self, request, *args, **kwargs):
        serializer = ProjectToTestCaseModelSerializer(instance=self.get_object())
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def projects_reports(self, request, *args, **kwargs):
        serializer = ProjectToReportsModelSerializer(instance=self.get_object())
        return Response(serializer.data)