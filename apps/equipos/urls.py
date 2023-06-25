from rest_framework.routers import DefaultRouter
from apps.equipos.views import EquipoModelViewSet

router = DefaultRouter()
router.register(r'equipos', EquipoModelViewSet)

urlpatterns = router.urls
