from utils.serializers import BaseModelSerializer
from apps.usuarios.models import Usuario

class UsuarioSerializer(BaseModelSerializer):
    """Serializer para los usuarios"""

    class Meta:
        model = Usuario
        fields = BaseModelSerializer.Meta.fields + (
            'first_name', 
            'last_name', 
            'sexo', 
            'peso', 
            'altura'
        )