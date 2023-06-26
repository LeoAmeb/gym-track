from django.db import models
from utils.models import BaseModel


class CatEjercicio(BaseModel):
    """Modelo para todos los ejercicios que se pueden hacer"""

    nombre = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to="ejercicios", blank=True, null=True)
    nombre = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = "catalogo de ejercicio"
        verbose_name_plural = "catalogos de ejercicios"

    def __str__(self):
        return self.nombre


class Ejercicio(BaseModel):
    """Modelo del ejercicio que realizó una persona"""

    estadistica = models.ForeignKey(
        "estadisticas.Estadistica",
        related_name="ejercicio_estadisticas",
        on_delete=models.CASCADE,
    )
    ejercicio = models.ForeignKey(
        CatEjercicio,
        related_name="ejercicio_catalogo",
        on_delete=models.CASCADE,
    )
    peso = models.FloatField(blank=True, null=True)
    series = models.IntegerField(blank=True, null=True)
    repeticiones = models.IntegerField(blank=True, null=True)
    distancia = models.FloatField(blank=True, null=True)
    duracion = models.TimeField(blank=True, null=True)
    puntaje = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "ejercicio"
        verbose_name_plural = "ejercicios"

    def __str__(self):
        return f"{self.estadistica.fecha} - {self.ejercicio.nombre}"
