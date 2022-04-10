from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from cases.models import CaseModel
from cases.serializer import CaseModelSerializer
from cases.serializer import CaseToReportModelSerializer
from rest_framework.viewsets import ModelViewSet
from .task import celery_test, celery_run_case
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import filters


class LargeResultsSetPagination(PageNumberPagination):
    """ 自定义分页 """
    page_size = 10  # 默认每页显示多少条数据
    max_page_size = 50  # 前端在控制每页显示多少条数据时，最多不能超过5
    page_query_param = 'page'  # 前端在查询字符串的关键字时，指定显示第几页的名字，不指定默认就是page
    page_size_query_param = 'page_size'  # 前端查询字符串的关键字名字，是用来控制每页显示多少条关键字


class CaseViewSet(ModelViewSet):
    # queryset = CaseModel.objects.filter(is_delete=False)
    queryset = CaseModel.objects.all().order_by('id')
    serializer_class = CaseModelSerializer

    # 过滤、排序
    filter_backends = [DjangoFilterBackend, OrderingFilter, filters.SearchFilter]
    # 指定过滤、排序的字段
    filterset_fields = ['id', 'create_time', 'project']
    search_fields = ['$name']

    # 指定分页类
    pagination_class = LargeResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CaseToReportModelSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CaseToReportModelSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def run(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        serializer = self.serializer_class(instance=instance, data=data)
        serializer.is_valid()
        testcase = serializer.data['testcase']

        # 运行用例
        celery_run_case(testcase, serializer)

        # 测试任务脚本
        # celery_test.delay()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # /case/allDel/?deleteid=1,2,3  多选删除
    @action(methods=['get'], detail=False)
    def allDel(self, request, *args, **kwargs):
        delete_id = request.query_params.get('deleteid', None)
        if not delete_id:
            return Response(status=status.HTTP_404_NOT_FOUND)
        for i in delete_id.split(','):
            CaseModel.objects.filter(id=i).delete()
        return Response(status=status.HTTP_200_OK)

    # /case/allRun/?runid=1,2,3  多选用例运行
    @action(methods=['get'], detail=False)
    def allRun(self, request, *args, **kwargs):
        run_id = request.query_params.get('runid', None)
        print(run_id)
        if not run_id:
            print(999)
            return Response(status=status.HTTP_404_NOT_FOUND)
        for i in run_id.split(','):
            instance = CaseModel.objects.get(id=i)
            testcase = instance.testcase
            serializer = self.get_serializer(instance)
            celery_run_case(testcase, serializer)
        return Response(status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def countTestCases(self, request, *args, **kwargs):
        count = self.get_queryset().count()
        return Response(count)