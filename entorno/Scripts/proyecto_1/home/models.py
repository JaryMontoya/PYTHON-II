# home/models.py

from django.db import models

class Contact(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)  # Cambia de vuelta

    def __str__(self):
        return self.nombre
