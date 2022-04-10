from django.urls import path
from .views import MemView
# from .views import MeninfoViewSet

urlpatterns = [
    path('', MemView.as_view()),
]

# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register('meninfo', MeninfoViewSet)
# urlpatterns = [
#
# ]
# urlpatterns += router.urls