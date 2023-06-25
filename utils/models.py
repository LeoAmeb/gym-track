from django.db import models


class BaseModel(models.Model):
    """Modelo base para todos los modelos del proyecto"""
    usuario_creo = models.ForeignKey(
        'usuarios.Usuario', related_name='%(class)s_usuario_creo', blank=True, null=True, on_delete=models.SET_NULL)
    usuario_edito = models.ForeignKey(
        'usuarios.Usuario', related_name='%(class)s_usuario_edito', blank=True, null=True, on_delete=models.SET_NULL)
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
