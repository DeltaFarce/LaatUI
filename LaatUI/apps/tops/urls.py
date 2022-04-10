from django.urls import path

from tops.views import TopView

urlpatterns = [
    path('', TopView.as_view()),
]