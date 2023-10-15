from django.shortcuts import render
from django.http import HttpResponse


#Dependencia para resolver apertura de archivos usando rutas relativas
from Excursiones.settings import BASE_DIR
import os



# Creacion de Clases basados en vistas

# login

# Create your views here.

def prueba_app(request):
    return render(request, "/authentication_app/templates/Appdos/index.html")

def prueba_salida(request):
    return HttpResponse("Hola-Bienvenidos")
