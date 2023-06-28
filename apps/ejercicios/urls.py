from rest_framework.routers import DefaultRouter
from apps.ejercicios.views import CatEjercicioModelViewSet, EjercicioModelViewSet

router = DefaultRouter()
router.register(r'catalogo-ejercicios', CatEjercicioModelViewSet)
router.register(r'ejercicios', EjercicioModelViewSet)

urlpatterns = router.urls
