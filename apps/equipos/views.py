from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import viewsets
from apps.equipos.models import Equipo
from apps.equipos.serializers import EquipoSerializer


class EquipoModelViewSet(viewsets.ModelViewSet):
    """Equipo ModelViewSet"""
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Equipo.objects.filter(activo=True)
    serializer_class = EquipoSerializer
