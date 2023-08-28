# Generated by Django 4.2.2 on 2023-06-26 03:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_edicion', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
                ('cantidad_ejercicios', models.IntegerField(blank=True, null=True)),
                ('duracion_entrenamiento', models.TimeField(blank=True, null=True)),
                ('duracion_sesion', models.TimeField(blank=True, null=True)),
                ('puntaje_total', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('hora_inicio', models.TimeField(blank=True, null=True)),
                ('hora_fin', models.TimeField(blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estadisticas_usuarios', to=settings.AUTH_USER_MODEL)),
                ('usuario_creo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_usuario_creo', to=settings.AUTH_USER_MODEL)),
                ('usuario_edito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_usuario_edito', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'estadistica',
                'verbose_name_plural': 'estadisticas',
            },
        ),
    ]