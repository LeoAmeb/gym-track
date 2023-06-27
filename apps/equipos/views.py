from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import viewsets
from apps.equipos.models import Equipo, EquipoIntegrante
from apps.equipos.serializers import EquipoSerializer, EquipoIntegranteSerializer


class EquipoModelViewSet(viewsets.ModelViewSet):
    """Equipo ModelViewSet"""
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = EquipoSerializer
    queryset = Equipo.objects.activos()

    def get_queryset(self):
        return self.queryset.filter(activo=True, usuario_creo=self.request.user)

    def perform_create(self, serializer):
        """Asigna el usuario que crea el equipo"""
        serializer.save(usuario_creo=self.request.user,
                        usuario_edito=self.request.user)


class EquipoIntegranteModelViewSet(viewsets.ModelViewSet):
    """EquipoIntegrante ModelViewSet"""
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = EquipoIntegranteSerializer
    queryset = EquipoIntegrante.objects.activos()

    def get_queryset(self):
        return self.queryset.filter(equipo__activo=True, user=self.request.user)
