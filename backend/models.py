from django.db import models

class Personaje(models.Model):
    nombre = models.CharField(max_length=50, unique=True, default="Sin nombre")
    x = models.IntegerField(default=50)
    y = models.IntegerField(default=50)
    velocidad = models.IntegerField(default=25)
    imagen = models.ImageField(upload_to='statics')

    def __str__(self):
        return self.nombre