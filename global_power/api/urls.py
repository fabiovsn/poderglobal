from rest_framework.routers import DefaultRouter
from .views import PoderGlobalViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'paises', PoderGlobalViewSet, basename='poder_global')

urlpatterns = router.urls