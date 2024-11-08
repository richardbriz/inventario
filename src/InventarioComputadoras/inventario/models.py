# inventario/models.py
from django.db import models
from django.contrib.auth.models import User

class Computadora(models.Model):
    responsable = models.CharField(max_length=200)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=100, unique=True)
    fecha_compra = models.DateField()
    licencia = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=[
        ('Disponible', 'Disponible'),
        ('En uso', 'En uso'),
        ('En reparación', 'En reparación'),
        ('Descartada', 'Descartada')
    ])

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.numero_serie}"
