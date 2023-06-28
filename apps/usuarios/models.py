from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords
from utils.models import BaseModel

# Create your models here.


class Usuario(AbstractUser, BaseModel):
    """Modelo de usuario extendido para usuarios personalizados."""
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )

    peso = models.FloatField()
    altura = models.FloatField()
    fecha_nacimiento = models.DateField(blank=True, null=True)
    foto = models.FileField(upload_to='usuarios/', blank=True, null=True)
    sexo = models.CharField(max_length=1)
    sexo_otro = models.CharField(max_length=50, blank=True, null=True)
    history = HistoricalRecords()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'sexo', 'peso', 'altura']

    def __str__(self):
        """Return username."""
        return self.username
