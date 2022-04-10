import os
from celery import Celery

project_name = os.path.split(os.path.abspath('.'))[-1]  # 获取项目名，本项目获取的就是LearnCelery
project_settings = '%s.settings' % project_name  # 获取该项目的settings文件，这里既是LearnCelery.settings

# 设置django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_settings)

# 实例化celery
app = Celery(project_name)

# 使用django的配置文件，进行配置
app.config_from_object('django.conf:settings')