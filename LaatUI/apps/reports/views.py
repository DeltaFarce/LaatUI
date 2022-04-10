from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from reports.models import ReportModel
from rest_framework.viewsets import ModelViewSet
from reports.serializer import ReportSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status


class LargeResultsSetPagination(PageNumberPagination):
    """ 自定义分页 """
    page_size = 10  # 默认每页显示多少条数据
    max_page_size = 50  # 前端在控制每页显示多少条数据时，最多不能超过5
    page_query_param = 'page'  # 前端在查询字符串的关键字时，指定显示第几页的名字，不指定默认就是page
    page_size_query_param = 'page_size'  # 前端查询字符串的关键字名字，是用来控制每页显示多少条关键字


class ReportViewSet(ModelViewSet):
    queryset = ReportModel.objects.filter(is_delete=False)
    serializer_class = ReportSerializer

    # 过滤、排序
    filter_backends = [DjangoFilterBackend, OrderingFilter, filters.SearchFilter]
    # 指定过滤、排序的字段
    filterset_fields = ['id', 'create_time', 'project']
    # 指定搜索字段
    search_fields = ['$name']

    # 指定分页类
    pagination_class = LargeResultsSetPagination

    @action(methods=['get'], detail=False)
    def countResport(self, request, *args, **kwargs):
        count = self.get_queryset().count()
        return Response(count)

    # /report/allDel/?deleteid=1,2,3  多选删除
    @action(methods=['get'], detail=False)
    def allDel(self, request, *args, **kwargs):
        delete_id = request.query_params.get('deleteid', None)
        if not delete_id:
            return Response(status=status.HTTP_404_NOT_FOUND)
        for i in delete_id.split(','):
            ReportModel.objects.filter(id=i).delete()
        return Response(status=status.HTTP_200_OK)