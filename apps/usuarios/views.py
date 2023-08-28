from django.shortcuts import render
from rest_framework import viewsets
from apps.usuarios.serializers import UsuarioSerializer
from apps.usuarios.models import Usuario

class UsuariosModelViewSet(viewsets.ModelViewSet):
    """Usuarios ModelViewSet"""
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

