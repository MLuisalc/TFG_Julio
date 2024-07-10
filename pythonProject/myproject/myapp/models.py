from django.db import models


class Denuncia(models.Model):
    ESTADO_CHOICES = [
        ('recibida', 'Recibida'),
        ('en_evaluacion', 'En evaluación'),
        ('en_investigacion', 'En investigación'),
        ('concluida', 'Concluida'),
    ]

    TIPIFICACION_CHOICES = [
        ('tipo1', 'Tipo 1'),
        ('tipo2', 'Tipo 2'),
        ('tipo3', 'Tipo 3'),
    ]

    VINCULO_CHOICES = [
        ('empleado_publico', 'Soy empleado público'),
        ('proveedor', 'Trabajo para una empresa proveedora'),
    ]

    hecho_denunciado = models.TextField()
    tipificacion_denuncia = models.CharField(max_length=100, choices=TIPIFICACION_CHOICES)
    nombre = models.CharField(max_length=100, blank=True)
    apellidos = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    correo = models.EmailField(blank=True)
    dni = models.CharField(max_length=20, blank=True)
    vinculo = models.CharField(max_length=100, choices=VINCULO_CHOICES)
    captcha = models.CharField(max_length=10)
    codigo_identificacion = models.CharField(max_length=10, unique=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='recibida')

    def __str__(self):
        return self.codigo_identificacion


class DenunciaArchivo(models.Model):
    denuncia = models.ForeignKey(Denuncia, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='archivos_denuncias/')
