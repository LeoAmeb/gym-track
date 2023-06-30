from django.db import models
from utils.models import BaseModel


class Estadistica(BaseModel):
    """Modelo para las estadisticas de los usuarios"""

    usuario = models.ForeignKey(
        "usuarios.Usuario",
        related_name="estadisticas_usuarios",
        on_delete=models.CASCADE,
    )
    cantidad_ejercicios = models.IntegerField(blank=True, null=True)
    duracion_entrenamiento = models.TimeField(blank=True, null=True)
    duracion_sesion = models.TimeField(blank=True, null=True)
    puntaje_total = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)

    class Meta:
        verbose_name = "estadistica"
        verbose_name_plural = "estadisticas"

        def __str__(self):
            return f"{self.usuario}: {self.fecha}"
        
    def set_cantidad_ejercicios(self):
        pass

    def set_duracion_entrenamiento(self):
        pass

    def set_puntaje_total(self):
       pass

    def compartir_estadisticas(self):
        pass 
