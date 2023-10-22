from django.db import models
#Importo el modelo User
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Viajes(models.Model):
    nombre = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    grupo = models.IntegerField()
    email= models.EmailField(max_length=80)
    info_document = models.CharField(null=True, max_length=300)
    imagen_viaj = models.ImageField(null=True, blank=True, upload_to="media")
    def __str__(self):
        return f"Nombre: {self.nombre.capitalize()}, Grupo: {self.grupo}, Email: {self.email}, Info: {self. info_document}, IMAGEN: {self.imagen_viaj}"

class Recreadores(models.Model):
   nombre = models.CharField(max_length=50)
   apellido = models.CharField(max_length=50)
   dni = models.IntegerField()
   edad = models.IntegerField()
   email= models.EmailField(max_length=80)
   info_document = models.CharField(null=True, max_length=300)
   imagen_viaj= models.ImageField(null=True, blank=True, upload_to="media")
   
   def __str__(self):
       return f"Nombre: {self.nombre.capitalize()}, Apellido: {self.apellido.capitalize()},  DNI: {self.dni}, Info: {self. info_document}, IMAGEN: {self.imagen}"
  
class Clientes(models.Model):
   nombre = models.CharField(max_length=50)
   apellido = models.CharField(max_length=50)
   dni = models.IntegerField()
   edad = models.IntegerField()
   email= models.EmailField(max_length=80)
   info_document = models.CharField(null=True, max_length=300)
   imagen_viaj= models.ImageField(null=True, blank=True, upload_to="media")
   def __str__(self):
       return f"Nombre: {self.nombre.capitalize()}, Apellido: {self.apellido.capitalize()},  DNI: {self.dni}, Info: {self. info_document}, IMAGEN: {self.imagen_viaj}"

class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    edad = models.IntegerField()
    email= models.EmailField(max_length=80) 
    info_document = models.CharField(null=True, max_length=300)
    imagen_viaj= models.ImageField(null=True, blank=True, upload_to="media")
    def __str__(self):
           return f"Nombre: {self.nombre.capitalize()}, Apellido: {self.apellido.capitalize()},  DNI: {self.dni}, Info: {self. info_document}, IMAGEN: {self.imagen_viaj}"

class Documentacion(models.Model):
    nombre = models.CharField(max_length=50)
    fechatope = models.DateField()
    entregado = models.BooleanField()
    email= models.EmailField(max_length=80)
    info_document = models.CharField(null=True, max_length=300)
    imagen_viaj= models.ImageField(null=True, blank=True, upload_to="media")
    def __str__(self):
           return f"Nombre: {self.nombre.capitalize()}, Fecha Tope: {self.fechatope},  Email: {self.email}, Info: {self. info_document},  IMAGEN: {self.imagen_viaj}"

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

#class Avatar(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    #def __str__(self):
           #return f"{settings.MEDIA_URL}{self.imagen}"