from django.db import models


class BaseModel(models.Model):
    """Modelo base para todos los modelos del proyecto"""
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-fecha_creacion', '-fecha_edicion']

    def desactivar(self, *args):
        self.activo = False
        self.save()
        return True

    def activar(self, *args):
        self.activo = True
        self.save()
        return True
