from django.db import models

# Create your models here.

class Usuario(models.Model):
  
    nombre = models.CharField(max_length=200)
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=200)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre.usuario

