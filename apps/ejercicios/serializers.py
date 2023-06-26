from rest_framework import serializers
from apps.ejercicios.models import CatEjercicio


class CatEjercicioSerializer(serializers.ModelSerializer):
    """Serializer para el catalogo de ejercicios"""

    class Meta:
        model = CatEjercicio
        fields = (
            "nombre",
            "imagen",
            "descripcion",
        )
