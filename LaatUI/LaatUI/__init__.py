# Python提供了__future__模块，把下一个新版本的特性导入到当前版本，于是我们就可以在当前版本中测试一些新版本的特性。举例说明如下：
# 为了适应Python 3.x的新的字符串的表示方法，在2.7版本的代码中，可以通过unicode_literals来使用Python 3.x的新的语法：
from __future__ import absolute_import, unicode_literals   # 我这里理解为unicode_literals防止.celery文件中的编码问题
# 这里.celery既是我们刚才新建的celery的实例化文件，倒出了我们实例化的app。并去别名为celery_app
from .celery import app as celery_app


import pymysql
pymysql.install_as_MySQLdb()


