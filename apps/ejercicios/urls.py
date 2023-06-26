from rest_framework.routers import DefaultRouter
from apps.ejercicios.views import CatEjercicioModelViewSet

router = DefaultRouter()
router.register(r'cat_ejercicios', CatEjercicioModelViewSet)

urlpatterns = router.urls
