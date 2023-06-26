from django.utils.timezone import now
from django.db import models


class DeactivateQuerySet(models.query.QuerySet):
    '''
    QuerySet whose delete() does not delete items, but instead marks the
    rows as not active, and updates the timestamps
    '''

    def delete(self):
        self.desactivar()

    def desactivar(self):
        return self.update(activo=False, fecha_edicion=now())

    def activar(self):
        return self.update(activo=True, fecha_edicion=now())

    def activos(self):
        return self.filter(activo=True)

    def inactivos(self):
        return self.filter(activo=False)


class DeactivateManager(models.Manager):
    '''
    Manager that returns a DeactivateQuerySet,
    to prevent object deletion.
    '''

    def get_query_set(self):
        return DeactivateQuerySet(self.model, using=self._db)

    def activos(self):
        return self.get_query_set().activos()

    def inactivos(self):
        return self.get_query_set().inactivos()


class BaseModel(models.Model):
    """Modelo base para todos los modelos del proyecto"""
    usuario_creo = models.ForeignKey(
        'usuarios.Usuario', related_name='%(class)s_usuario_creo', blank=True, null=True, on_delete=models.SET_NULL)
    usuario_edito = models.ForeignKey(
        'usuarios.Usuario', related_name='%(class)s_usuario_edito', blank=True, null=True, on_delete=models.SET_NULL)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    objects = DeactivateManager()

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
