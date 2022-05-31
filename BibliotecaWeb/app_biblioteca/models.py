from django.db import models

# Create your models here.

class Bibliotecario(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Alumno(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    n_libreta = models.IntegerField() # numero de libreta universitaria


class Libro(models.Model):
    titulo =models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    años_publicacion = models.IntegerField()
    numeros_ejemplares= models.IntegerField()



class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    dni = models.IntegerField()  # numero de libreta universitaria

