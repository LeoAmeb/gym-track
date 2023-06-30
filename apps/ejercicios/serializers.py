from utils.serializers import BaseModelSerializer
from apps.ejercicios.models import CatEjercicio, Ejercicio


class CatEjercicioSerializer(BaseModelSerializer):
    """Serializer para el catalogo de ejercicios"""

    class Meta:
        model = CatEjercicio
        fields = BaseModelSerializer.Meta.fields + (
            "nombre",
            "imagen",
            "descripcion",
        )


class EjercicioSerializer(BaseModelSerializer):
    """Serializer para ejercicios"""

    class Meta:
        model = Ejercicio
        fields = BaseModelSerializer.Meta.fields + (
            "estadistica",
            "ejercicio",
            "peso",
            "series",
            "repeticiones",
            "distancia",
            "duracion",
            "puntaje",
        )
