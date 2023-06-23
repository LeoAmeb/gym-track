from django.contrib import admin
from apps.equipos.models import Equipo, EquipoIntegrante

# Register your models here.


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    pass


@admin.register(EquipoIntegrante)
class EquipoIntegranteAdmin(admin.ModelAdmin):
    pass
