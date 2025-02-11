# Generated by Django 5.0.6 on 2024-07-07 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hecho_denunciado', models.TextField()),
                ('tipificacion_denuncia', models.CharField(max_length=100)),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('apellidos', models.CharField(blank=True, max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('correo', models.EmailField(blank=True, max_length=254)),
                ('dni', models.CharField(blank=True, max_length=20)),
                ('vinculo', models.CharField(max_length=100)),
                ('captcha', models.CharField(max_length=10)),
                ('codigo_identificacion', models.CharField(max_length=10, unique=True)),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('recibida', 'Recibida'), ('en_evaluacion', 'En evaluación'), ('en_investigacion', 'En investigación'), ('concluida', 'Concluida')], default='recibida', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DenunciaArchivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='archivos_denuncias/')),
                ('denuncia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.denuncia')),
            ],
        ),
    ]
