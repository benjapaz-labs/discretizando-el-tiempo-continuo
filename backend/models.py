from django.db import models

class Personaje(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    velocidad = models.IntegerField(default=0)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    imagen = models.CharField(max_length=255, default="")  # Ruta de la imagen

    def __str__(self):
        return self.nombre