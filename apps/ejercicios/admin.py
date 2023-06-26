from django.contrib import admin
from apps.ejercicios.models import CatEjercicio, Ejercicio

@admin.register(CatEjercicio)
class CatEjercicioAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)
    list_filter = ("activo",)
    list_display = ("nombre", "descripcion")
    fields = ("nombre", "descripcion", "imagen")
    raw_id_fields = ("usuario_creo", "usuario_edito",)
    readonly_fields = ("fecha_creacion", "fecha_edicion",)
