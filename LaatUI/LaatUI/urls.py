"""LaatUI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Swagger接口文档平台',
        default_version='v1',
        description='这是一个接口文档',
        terms_of_service='http://127.0.0.1',
        contact=openapi.Contact(email='xxxxxx@163.com'),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny)#权限类
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('', include('cases.urls')),
    path('', include('reports.urls')),
    path('net', include('nets.urls')),
    path('mem', include('meninfo.urls')),
    path('cpu', include('cpus.urls')),
    path('df', include('dfs.urls')),
    path('load', include('loads.urls')),
    path('top', include('tops.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-json')
]
