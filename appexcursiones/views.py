from django.shortcuts import render, redirect
from django.http import HttpResponse
from appexcursiones.forms import ViajeFormulario, RecreadorFormulario, ClienteFormulario, ProveedorFormulario,  DocumentacionFormulario, UserRegisterForm,  UserEditForm, AvatarForm
from appexcursiones.models import Viajes, Recreadores, Clientes, Proveedores, Documentacion, Avatar   


#Dependencia para resolver apertura de archivos usando rutas relativas
from Excursiones.settings import BASE_DIR
import os



# Creacion de Clases basados en vistas
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 

# login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url
        
    else:
        imagen_url = ""
    return render(request, "Appnuevo/inicio.html", {"imagen_url": imagen_url})

def viajes(request):
    errores = ""
    
    #Validamos tipo de validacion
    if request.method == "POST":
        #Cargamos los datos en el formulario
        formulario = ViajeFormulario(request.POST)
        
        #Validamos los datos
        if formulario.is_valid():
            
            #Recuperamos los Datos
            data = formulario.cleaned_data
            #Creamos el viaje
            viaje = Viajes(nombre=data["nombre"], destino=data["destino"], grupo=data["grupo"], email=data["email"])
            #Guardamos el viaje
            viaje.save()
        else:
            #Si el formulario no es valido, guardamos los errores para mostrarlos
            errores = formulario.errors
            
    #Recuperar todos los cursos de la BD
    viajes = Viajes.objects.all() 
    
    #Creamos el formulario vacio
    formulario = ViajeFormulario()
    
    #Creamos el contexto
    contexto = {"listado_viajes":viajes, "formulario": formulario, "errores":errores}
    
    #Retornamos la repuesta
    return render(request, "Appnuevo/viajes.html", contexto)

def editar_viajes(request, id):
    viaje = Viajes.objects.get(id=id)
       
    #Validamos tipo de validacion
    if request.method == "POST":
                   
        #Cargamos los datos en el formulario
        formulario = ViajeFormulario(request.POST)
            
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            #Editamos el viaje
            viaje.nombre = data["nombre"]
            viaje.grupo = data["grupo"]
            # Guardamos el formulario
            viaje.save()
            return redirect("proyecto-viajes")
        else:
            #Retornamos la repuesta
            return render(request, "Appnuevo/editar_viajes.html", {"formulario": formulario, "errores": formulario.errors})
    else:
        formulario = ViajeFormulario(initial={"nombre":viaje.nombre, "grupo":viaje.grupo})
        return render(request, "Appnuevo/editar_viajes.html",{"formulario":formulario, "errores": ""})

def buscar_viajes(request):
    return render(request, "Appnuevo/busqueda_viajes.html")

def resultados_buscar_viajes(request):
    nombre_viaje= request.GET["nombre_viaje"]
    viajes = Viajes.objects.filter(nombre__icontains=nombre_viaje)
    return render(request, "Appnuevo/resultados_busquedas_viajes.html", {"viajes":viajes})

def eliminar_viajes(request, id):
    #Trae todos los viajes
    viaje = Viajes.objects.get(id=id)
    viaje.delete()
    return redirect("proyecto-viajes")
    
def recreadores(request):
    return render(request, "Appnuevo/recreadores.html")


def creacion_recreadores(request):
    if request.method =="POST":
        formulario = RecreadorFormulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            #
            recreadores = Recreadores(nombre=data["nombre"], apellido=data["apellido"], dni=data["dni"], edad=data["edad"], email=data["email"])
            # Guardamos el formulario
            recreadores.save()
    
    formulario = RecreadorFormulario()
    contexto = {"formulario": formulario} 
    return render(request, "Appnuevo/recreadores_formularios.html", contexto)

def leer_recreadores(request):
    #Trae todos los viajes
    recreadores = Recreadores.objects.all()
    contexto = {"recreadores":recreadores}
    return render(request, "Appnuevo/leerrecreadores.html", contexto)

def clientes(request):
    return render(request, "Appnuevo/clientes.html")


def creacion_clientes(request):
    if request.method =="POST":
        formulario = ClienteFormulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            #
            clientes = Clientes(nombre=data["nombre"], apellido=data["apellido"], dni=data["dni"], edad=data["edad"], email=data["email"])
            # Guardamos el formulario
            clientes.save()
    
    formulario = ClienteFormulario()
    contexto = {"formulario": formulario} 
    return render(request, "Appnuevo/clientes_formularios.html", contexto)

def leer_clientes(request):
    #Trae todos los viajes
    clientes = Clientes.objects.all()
    contexto = {"clientes":clientes}
    return render(request, "Appnuevo/leerclientes.html", contexto)

def proveedores(request):
    return render(request, "Appnuevo/proveedores.html")

def creacion_proveedores(request):
    if request.method =="POST":
        formulario = ProveedorFormulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            #
            proveedores = Proveedores(nombre=data["nombre"], apellido=data["apellido"], dni=data["dni"], edad=data["edad"], email=data["email"])
            # Guardamos el formulario
            proveedores.save()
    
    formulario = ProveedorFormulario()
    contexto = {"formulario": formulario}  
    return render(request, "Appnuevo/proveedores_formularios.html", contexto)

def leer_proveedores(request):
    #Trae todos los viajes
    proveedores = Proveedores.objects.all()
    contexto = {"proveedores":proveedores}
    return render(request, "Appnuevo/leerproveedores.html", contexto)


def documentacion(request):
    return render(request, "Appnuevo/documentacion.html")

def creacion_documentacion(request):
    if request.method =="POST":
        formulario = DocumentacionFormulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            #
            documentacion = Documentacion(nombre=data["nombre"], fechatope=data["fechatope"], entregado=data["entregado"], email=data["email"])
            # Guardamos el formulario
            documentacion.save()
    
    formulario = DocumentacionFormulario()
    contexto = {"formulario": formulario} 
    return render(request, "Appnuevo/documentacion_formularios.html", contexto)

def leer_documentacion(request):
    #Trae todos los viajes
    documentacion = Documentacion.objects.all()
    contexto = {"documentacion":documentacion}
    return render(request, "Appnuevo/leerdocumentacion.html", contexto)


class DocumentacionList(LoginRequiredMixin, ListView):
    model = Documentacion
    template_name = "Appnuevo/list_documentacion.html"

class DocumentacionDetail(DetailView):
    model = Documentacion
    template_name = "Appnuevo/detail_documentacion.html"
    
class DocumentacionCreate(CreateView):
    model = Documentacion
    success_url = "/proyecto/documentacion/"
    fields = ["nombre", "fechatope", "entregado", "email"]
    template_name = "Appnuevo/documentacion_form.html"
    
class DocumentacionUpdate(UpdateView):
    model = Documentacion
    success_url = "/proyecto/documentacion/"
    fields = ["nombre", "fechatope", "entregado", "email"]
    template_name = "Appnuevo/documentacion_form.html"
class DocumentacionDelete(DeleteView):
    model = Documentacion
    success_url = "/proyecto/documentacion/"
    template_name = "Appnuevo/documentacion_confirm_delete.html" 

        
