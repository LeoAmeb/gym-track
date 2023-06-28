from django.db import models
from simple_history.models import HistoricalRecords
from utils.models import BaseModel


class Equipo(BaseModel):
    """Modelo para grupos de entrenamiento"""
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='grupos', blank=True, null=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'equipo'
        verbose_name_plural = 'equipos'

    def __str__(self):
        return self.nombre


class EquipoIntegrante(BaseModel):
    """Modelo para integrantes de equipos"""
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    integrante = models.ForeignKey(
        'usuarios.Usuario', related_name='equipos_integrantes', on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    admin = models.BooleanField(default=False)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'equipo integrante'
        verbose_name_plural = 'equipos integrantes'
        unique_together = ('equipo', 'integrante')

    def __str__(self):
        return self.equipo.nombre + ' - ' + self.integrante.username
