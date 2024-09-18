from .views import TrackerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TrackerViewSet, basename='tracker')
urlpatterns = router.urls
