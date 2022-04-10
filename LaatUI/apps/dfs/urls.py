from django.urls import path

from dfs.views import DfView

urlpatterns = [
    path('', DfView.as_view()),
]