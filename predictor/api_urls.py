
from rest_framework.routers import DefaultRouter
from .api_views import PredictionViewSet

router = DefaultRouter()

router.register(
    r'predictions',
    PredictionViewSet,
    basename='prediction'
)

urlpatterns = router.urls
