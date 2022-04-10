from rest_framework import routers

from cases.views import CaseViewSet

router = routers.DefaultRouter()
router.register('cases', CaseViewSet)
urlpatterns = [

]
urlpatterns += router.urls