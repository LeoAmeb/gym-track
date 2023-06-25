from rest_framework import serializers
from apps.equipos.models import Equipo, EquipoIntegrante


class EquipoSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Equipo"""
    class Meta:
        model = Equipo
        fields = (
            'id',
            'nombre',
            'descripcion',
            'imagen',
            'activo',
            'fecha_creacion',
            'fecha_edicion',
        )


class EquipoIntegranteSerializer(serializers.ModelSerializer):
    """Serializer para el modelo EquipoIntegrante"""
    class Meta:
        model = EquipoIntegrante
        fields = (
            'id',
            'equipo',
            'integrante',
            'fecha_ingreso',
            'admin',
            'activo',
            'fecha_creacion',
            'fecha_edicion',
        )
