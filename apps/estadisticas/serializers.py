from utils.serializers import BaseModelSerializer
from apps.estadisticas.models import Estadistica


class EstadisticaSerializer(BaseModelSerializer):
    """Serializer para las estadisticas"""

    class Meta:
        model = Estadistica
        fields = BaseModelSerializer.Meta.fields + (
            "usuario",
            "cantidad_ejercicios",
            "duracion_entrenamiento",
            "duracion_sesion",
            "puntaje_total",
            "fecha",
            "hora_inicio",
            "hora_fin",
        )
