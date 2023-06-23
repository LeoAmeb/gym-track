from django.db import models
from utils.models import BaseModel


class Equipo(BaseModel):
    """Modelo para grupos de entrenamiento"""
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='grupos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'equipo'
        verbose_name_plural = 'equipos'

    def __str__(self):
        return self.nombre
