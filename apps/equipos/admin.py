from django.contrib import admin
from apps.equipos.models import Equipo

# Register your models here.


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    pass
