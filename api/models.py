from django.db import models

# Create your models here.
class curso(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    url_imagen = models.CharField(max_length=100)

class curso2(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    url_imagen = models.CharField(max_length=100)
    institucion = models.CharField(max_length=50)
