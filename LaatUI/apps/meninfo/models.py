from django.db import models


class Meminfo(models.Model):
    name = models.CharField(help_text="项目名", verbose_name="项目名", max_length=200)