from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import viewsets
from apps.ejercicios.models import CatEjercicio, Ejercicio
from apps.ejercicios.serializers import CatEjercicioSerializer, EjercicioSerializer

class CatEjercicioModelViewSet(viewsets.ModelViewSet):
    """ModelViewSet para el catalogo de ejercicios"""
    queryset = CatEjercicio.objects.all()
    serializer_class = CatEjercicioSerializer

class EjercicioModelViewSet(viewsets.ModelViewSet):
    """ModelViewSet para los ejercicios"""
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer