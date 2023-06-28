from utils.serializers import BaseModelSerializer
from apps.equipos.models import Equipo, EquipoIntegrante


class EquipoSerializer(BaseModelSerializer):
    """Serializer para el modelo Equipo"""
    class Meta:
        model = Equipo
        fields = BaseModelSerializer.Meta.fields + (
            'nombre',
            'descripcion',
            'imagen',
        )


class EquipoIntegranteSerializer(BaseModelSerializer):
    """Serializer para el modelo EquipoIntegrante"""
    class Meta:
        model = EquipoIntegrante
        fields = BaseModelSerializer.Meta.fields + (
            'equipo',
            'integrante',
            'fecha_ingreso',
            'admin',
        )
