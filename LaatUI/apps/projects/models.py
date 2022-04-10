from django.db import models


class ProjectModel(models.Model):
    objects = None
    id = models.AutoField(verbose_name="Id主键", primary_key=True, help_text="Id主键")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除", help_text="逻辑删除")
    name = models.CharField(verbose_name="项目名称", max_length=200, unique=True, help_text="项目名称")
    desc = models.TextField(verbose_name="描述", help_text="描述", default='')

    class Meta:
        db_table = 'tb_projects'
        verbose_name = '项目信息'
        verbose_name_plural = '项目信息'

    def __str__(self):
        return self.name

