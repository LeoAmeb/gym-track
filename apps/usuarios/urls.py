from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from apps.usuarios.views import UsuariosModelViewSet

urlpatterns = [
    # Auth URLs
    path('auth/', include([
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ]))
]

router = DefaultRouter()
router.register(r"usuarios-crud", UsuariosModelViewSet, basename="usuarios-crud")

urlpatterns += router.urls