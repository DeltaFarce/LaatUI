from rest_framework import routers

from reports.views import ReportViewSet

router = routers.DefaultRouter()
router.register('reports', ReportViewSet)
urlpatterns = [

]
urlpatterns += router.urls