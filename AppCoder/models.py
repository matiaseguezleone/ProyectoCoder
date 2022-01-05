from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField('nombre', max_length=50)
    camada = models.IntegerField()

class Profesor(models.Model):

    nombre = models.CharField('nombre', max_length=40)
    apellido = models.CharField('apellido', max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Estudiante(models.Model):
    nombre = models.CharField('nombre', max_length=40)
    apellido = models.CharField('apellido', max_length=40)

class Entregable(models.Model):
    nombre = models.CharField('nombre', max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField() 
