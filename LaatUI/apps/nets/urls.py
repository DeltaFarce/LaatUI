from django.urls import path

from nets.views import NetView

urlpatterns = [
    path('', NetView.as_view()),
]