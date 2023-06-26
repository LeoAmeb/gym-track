from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    """Base serializer"""
    activo = serializers.BooleanField(default=True)

    class Meta:
        fields = (
            'id',
            'activo',
            'fecha_creacion',
            'fecha_edicion',
        )
