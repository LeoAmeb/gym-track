from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # API Urls
    path('api/', include([
        path('', include('apps.equipos.urls')),
        path('usuarios/', include('apps.usuarios.urls')),
    ])),
]
