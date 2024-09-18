from .views import CustomerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CustomerViewSet, basename='customer')
urlpatterns = router.urls
