from django.urls import path

from cpus.views import CpuView

urlpatterns = [
    path('', CpuView.as_view()),
]