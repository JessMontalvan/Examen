from django.db import models

# Create your models here.
class User(models.Model):
  
    usuario = models.CharField(max_length=100)
    inicio = models.CharField(max_length=200)
    fin = models.IntegerField()

    def __str__(self):
        return self.nombre.inicio