from django.db import models
#Importo el modelo User
from django.contrib.auth.models import User

# Create your models here.

class Viajes(models.Model):
    nombre = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    grupo = models.IntegerField()
    email= models.EmailField(max_length=80)
    imagen_viaj= models.ImageField(null=True, blank=True, upload_to="viajes")
    def __str__(self):
        return f"Nombre: {self.nombre.capitalize()}, Grupo: {self.grupo}, Email: {self.email}"

class Recreadores(models.Model):
   nombre = models.CharField(max_length=50)
   apellido = models.CharField(max_length=50)
   dni = models.IntegerField()
   edad = models.IntegerField()
   email= models.EmailField(max_length=80)
   def __str__(self):
       return f"Nombre: {self.nombre.capitalize()}, Apellido: {self.apellido.capitalize()},  DNI: {self.dni}"
  
class Clientes(models.Model):
   nombre = models.CharField(max_length=50)
   apellido = models.CharField(max_length=50)
   dni = models.IntegerField()
   edad = models.IntegerField()
   email= models.EmailField(max_length=80)
   def __str__(self):
       return f"Nombre: {self.nombre.capitalize()}, Apellido: {self.apellido.capitalize()},  DNI: {self.dni}"

class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    edad = models.IntegerField()
    email= models.EmailField(max_length=80) 
    def __str__(self):
           return f"Nombre: {self.nombre.capitalize()}, Apellido: {self.apellido.capitalize()},  DNI: {self.dni}"

class Documentacion(models.Model):
    nombre = models.CharField(max_length=50)
    fechatope = models.DateField()
    entregado = models.BooleanField()
    email= models.EmailField(max_length=80)
    def __str__(self):
           return f"Nombre: {self.nombre.capitalize()}, Fecha Tope: {self.fechatope},  Email: {self.email}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
