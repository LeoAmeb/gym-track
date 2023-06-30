from rest_framework import viewsets
from apps.estadisticas.models import Estadistica
from apps.estadisticas.serializers import EstadisticaSerializer

class EstadisticaModelViewSet(viewsets.ModelViewSet):
    """ModelViewSet para las estadisticas"""
    queryset = Estadistica.objects.all()
    serializer_class = EstadisticaSerializer