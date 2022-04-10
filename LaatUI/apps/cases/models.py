from django.db import models
from projects.models import ProjectModel


class CaseModel(models.Model):
    objects = None
    id = models.AutoField(verbose_name="Id主键", primary_key=True, help_text="Id主键")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除", help_text="逻辑删除")
    name = models.CharField(verbose_name="用例名称", max_length=200, unique=True, help_text="用例名称")
    testcase = models.TextField(verbose_name="测试脚本", help_text="测试脚本")
    desc = models.TextField(verbose_name="用例描述", help_text="用例描述", default='')
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='case', verbose_name="所属项目", help_text='所属项目')

    class Meta:
        db_table = 'tb_cases'
        verbose_name = '用例信息'
        verbose_name_plural = '用例信息'

    def __str__(self):
        return self.name