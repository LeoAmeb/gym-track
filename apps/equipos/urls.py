from rest_framework.routers import DefaultRouter
from apps.equipos.views import EquipoModelViewSet, EquipoIntegranteModelViewSet

router = DefaultRouter()
router.register(r'equipos', EquipoModelViewSet)
router.register(r'equipos-integrantes', EquipoIntegranteModelViewSet)

urlpatterns = router.urls
