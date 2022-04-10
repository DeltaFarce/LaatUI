from django.db import models
from projects.models import ProjectModel
from cases.models import CaseModel


class ReportModel(models.Model):
    objects = None
    id = models.AutoField(verbose_name="Id主键", primary_key=True, help_text="Id主键")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除", help_text="逻辑删除")
    name = models.CharField(verbose_name="报告名称", max_length=200, unique=True, help_text="报告名称")
    state = models.CharField(verbose_name="状态", max_length=20, help_text="状态", default="成功")
    log = models.TextField(verbose_name="用例日志", help_text="用例日志", default='')
    screenshot = models.TextField(verbose_name="描述", help_text="描述", default='')
    video = models.TextField(verbose_name="描述", help_text="描述", default='')
    case = models.ForeignKey(CaseModel, on_delete=models.CASCADE, help_text="所属用例", related_name='case', verbose_name="所属用例")
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='report', help_text="所属项目", verbose_name="所属项目")

    class Meta:
        db_table = 'tb_reports'
        verbose_name = '报告信息'
        verbose_name_plural = '报告信息'

    def __str__(self):
        return self