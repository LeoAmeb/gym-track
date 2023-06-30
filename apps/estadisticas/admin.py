from django.contrib import admin
from apps.estadisticas.models import Estadistica


@admin.register(Estadistica)
class EstadisticasAdmin(admin.ModelAdmin):
    search_fields = ("usuario", "fecha")
    list_filter = ("activo",)
    list_display = (
        "usuario",
        "cantidad_ejercicios",
        "duracion_entrenamiento",
        "duracion_sesion",
        "puntaje_total",
        "fecha",
        "hora_inicio",
        "hora_fin",
    )
    fields = (
        "usuario",
        "cantidad_ejercicios",
        "duracion_entrenamiento",
        "duracion_sesion",
        "puntaje_total",
        "fecha",
        "hora_inicio",
        "hora_fin",
    )
    raw_id_fields = (
        "usuario_creo",
        "usuario_edito",
        "usuario"
    )
    readonly_fields = (
        "fecha_creacion",
        "fecha_edicion",
    )
