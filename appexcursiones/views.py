from django.shortcuts import render, redirect
from django.http import HttpResponse
from appexcursiones.forms import ViajeFormulario,  UserRegisterForm,  UserEditForm, AvatarForm
#from appexcursiones.forms import ViajeFormulario, RecreadorFormulario, ClienteFormulario, ProveedorFormulario, UserRegisterForm,  UserEditForm, AvatarForm
from appexcursiones.models import Viajes, Recreadores, Clientes, Proveedores, Documentacion, Avatar   
from django.urls import reverse_lazy

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

@login_required  
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
            viaje = Viajes(nombre=data["nombre"], destino=data["destino"], grupo=data["grupo"], email=data["email"], imagen_viaj=data["imagen"])
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
    contexto = {"listado_viajes": viajes, "formulario": formulario, "errores":errores}
    
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
#----------------------------------------------------------------------------------------#    

class RecreadoresListViews(LoginRequiredMixin, ListView):
    model = Recreadores
    template_name = "Appnuevo/recreadores_list.html"

class RecreadoresDetailViews(LoginRequiredMixin, DetailView):
    model = Recreadores
    template_name = "Appnuevo/recreadores_detail.html"
    
class RecreadoresCreateView(LoginRequiredMixin, CreateView):
    model = Recreadores
    template_name = "Appnuevo/recreadores_create.html"
    fields = ["nombre", "apellido", "dni", "edad",  "email"]
    success_url = reverse_lazy("proyecto-recreadores-list")
    
class RecreadoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Recreadores
    success_url = reverse_lazy("proyecto-recreadores-list")
    fields = ["nombre", "apellido", "dni", "edad",  "email"]
    template_name = "Appnuevo/recreadores_update.html"

class RecreadoresDeleteView(DeleteView):
    model = Recreadores
    success_url = reverse_lazy("proyecto-recreadores-list")
    template_name = "Appnuevo/recreadores_confirm_delete.html" 


#--------------------------------------------------------------------------------------------#

class ClientesListViews(LoginRequiredMixin, ListView):
    model = Clientes
    template_name = "Appnuevo/clientes_list.html"

class ClientesDetailViews(LoginRequiredMixin, DetailView):
    model = Clientes
    template_name = "Appnuevo/clientes_detail.html"
    
class ClientesCreateView(LoginRequiredMixin, CreateView):
    model = Clientes
    template_name = "Appnuevo/clientes_create.html"
    fields = ["nombre", "apellido", "dni", "edad",  "email"]
    success_url = reverse_lazy("proyecto-clientes-list")
    
class ClientesUpdateView(LoginRequiredMixin, UpdateView):
    model = Clientes
    success_url = reverse_lazy("proyecto-clientes-list")
    fields = ["nombre", "apellido", "dni", "edad",  "email"]
    template_name = "Appnuevo/clientes_update.html"

class ClientesDeleteView(DeleteView):
    model = Clientes
    success_url = reverse_lazy("proyecto-clientes-list")
    template_name = "Appnuevo/clientes_confirm_delete.html" 


#--------------------------------------------------------------------------------------------#

class ProveedoresListViews(LoginRequiredMixin, ListView):
    model = Proveedores
    template_name = "Appnuevo/proveedores_list.html"

class ProveedoresDetailViews(LoginRequiredMixin, DetailView):
    model = Proveedores
    template_name = "Appnuevo/proveedores_detail.html"
    
class ProveedoresCreateView(LoginRequiredMixin, CreateView):
    model = Proveedores
    template_name = "Appnuevo/proveedores_create.html"
    fields = ["nombre", "apellido", "dni", "edad",  "email"]
    success_url = reverse_lazy("proyecto-proveedores-list")
    
class ProveedoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Proveedores
    success_url = reverse_lazy("proyecto-proveedores-list")
    fields = ["nombre", "apellido", "dni", "edad",  "email"]
    template_name = "Appnuevo/proveedores_update.html"

class ProveedoresDeleteView(DeleteView):
    model = Proveedores
    success_url = reverse_lazy("proyecto-proveedores-list")
    template_name = "Appnuevo/proveedores_confirm_delete.html" 


#--------------------------------------------------------------------------------------------#

class DocumentacionList(LoginRequiredMixin, ListView):
    model = Documentacion
    template_name = "Appnuevo/documentacion_list.html"

class DocumentacionDetail(DetailView):
    model = Documentacion
    template_name = "Appnuevo/documentacion_detail.html"
    
class DocumentacionCreate(CreateView):
    model = Documentacion
    template_name = "Appnuevo/documentacion_create.html"
    fields = ["nombre", "fechatope", "entregado", "email"]
    success_url = reverse_lazy("proyecto-documentacion-list")
    
class DocumentacionUpdate(LoginRequiredMixin, UpdateView):
    model = Documentacion
    success_url = "proyecto-documentacion-list"
    fields = ["nombre", "fechatope", "entregado", "email"]
    template_name = "Appnuevo/documentacion_update.html"
class DocumentacionDelete(DeleteView):
    model = Documentacion
    success_url = reverse_lazy("proyecto-documentacion-list")
    template_name = "Appnuevo/documentacion_confirm_delete.html"
        
