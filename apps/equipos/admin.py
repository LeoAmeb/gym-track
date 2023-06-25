from django.contrib import admin
from apps.equipos.models import Equipo, EquipoIntegrante


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)
    list_filter = ("activo",)
    list_display = (
        "nombre",
        "descripcion",
        "imagen",
        "activo",
        "fecha_creacion",
        "fecha_edicion",
    )
    fields = (
        "nombre",
        "descripcion",
        "imagen",
        "usuario_creo",
        "usuario_edito",
        "activo",
        "fecha_creacion",
        "fecha_edicion",
    )
    raw_id_fields = ("usuario_creo", "usuario_edito",)
    readonly_fields = ("fecha_creacion", "fecha_edicion",)


@admin.register(EquipoIntegrante)
class EquipoIntegranteAdmin(admin.ModelAdmin):
    search_fields = (
        "equipo__nombre",
        "integrante__name",
        "integrante__last_name",
        "integrante__username",
        "integrante__email"
    )
    list_filter = ("admin", "activo", "fecha_ingreso",)
    list_display = (
        "equipo",
        "integrante",
        "fecha_ingreso",
        "admin",
        "activo",
        "fecha_creacion",
        "fecha_edicion",
    )
    fields = (
        "equipo",
        "integrante",
        "fecha_ingreso",
        "admin",
        "usuario_creo",
        "usuario_edito",
        "activo",
        "fecha_creacion",
        "fecha_edicion",
    )
    readonly_fields = ("fecha_creacion", "fecha_edicion",)
    raw_id_fields = ("equipo", "integrante", "usuario_creo", "usuario_edito",)
