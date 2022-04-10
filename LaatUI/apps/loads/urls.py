from django.urls import path

from loads.views import LoadView

urlpatterns = [
    path('', LoadView.as_view()),
]