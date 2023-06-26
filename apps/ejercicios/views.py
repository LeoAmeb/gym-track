from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import viewsets
from apps.ejercicios.models import CatEjercicio
from apps.ejercicios.serializers import CatEjercicioSerializer

class CatEjercicioModelViewSet(viewsets.ModelViewSet):
    """ModelViewSet para el catalogo de ejercicios"""
    queryset = CatEjercicio.objects.all()
    serializer_class = CatEjercicioSerializer