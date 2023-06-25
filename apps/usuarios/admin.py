from django.contrib import admin
from apps.usuarios.models import Usuario

# Register your models here.


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass
