# Generated by Django 4.2.2 on 2023-06-25 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_edicion', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='grupos')),
            ],
            options={
                'verbose_name': 'equipo',
                'verbose_name_plural': 'equipos',
            },
        ),
        migrations.CreateModel(
            name='EquipoIntegrante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_edicion', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_ingreso', models.DateField()),
                ('admin', models.BooleanField(default=False)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.equipo')),
            ],
            options={
                'verbose_name': 'equipo integrante',
                'verbose_name_plural': 'equipos integrantes',
            },
        ),
    ]
