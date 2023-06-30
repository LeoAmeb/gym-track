from rest_framework.routers import DefaultRouter
from apps.estadisticas.views import EstadisticaModelViewSet

router = DefaultRouter()
router.register(r"estadisticas", EstadisticaModelViewSet)

urlpatterns = router.urls
