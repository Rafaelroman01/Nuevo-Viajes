from django.shortcuts import render, redirect
from django.http import HttpResponse
from appexcursiones.forms import UserRegisterForm,  UserEditForm, AvatarForm
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

#----------------------------------------------------------------------------------------#    

class ViajesListViews(LoginRequiredMixin, ListView):
    model = Viajes
    template_name = "Appnuevo/viajes_list.html"

class ViajesDetailViews(LoginRequiredMixin, DetailView):
    model = Viajes
    template_name = "Appnuevo/viajes_detail.html"
    
class ViajesCreateView(LoginRequiredMixin, CreateView):
    model = Viajes
    template_name = "Appnuevo/viajes_create.html"
    fields = ["nombre", "destino", "grupo",  "email","imagen_viaj"]
    success_url = reverse_lazy("proyecto-viajes-list")
    
class ViajesUpdateView(LoginRequiredMixin, UpdateView):
    model = Viajes
    success_url = reverse_lazy("proyecto-viajes-list")
    fields = ["nombre", "destino", "grupo",  "email","imagen_viaj"]
    template_name = "Appnuevo/viajes_update.html"

class ViajesDeleteView(DeleteView):
    model = Viajes
    success_url = reverse_lazy("proyecto-viajes-list")
    template_name = "Appnuevo/viajes_confirm_delete.html" 


#-----------------------------------------------------------------------------
class RecreadoresListViews(LoginRequiredMixin, ListView):
    model = Recreadores
    template_name = "Appnuevo/recreadores_list.html"

class RecreadoresDetailViews(LoginRequiredMixin, DetailView):
    model = Recreadores
    template_name = "Appnuevo/recreadores_detail.html"
    
class RecreadoresCreateView(LoginRequiredMixin, CreateView):
    model = Recreadores
    template_name = "Appnuevo/recreadores_create.html"
    fields = ["nombre", "apellido", "dni", "edad",  "email", "imagen_viaj"]
    success_url = reverse_lazy("proyecto-recreadores-list")
    
class RecreadoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Recreadores
    success_url = reverse_lazy("proyecto-recreadores-list")
    fields = ["nombre", "apellido", "dni", "edad",  "email", "imagen_viaj"]
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
    fields = ["nombre", "apellido", "dni", "edad",  "email", "imagen_viaj"]
    success_url = reverse_lazy("proyecto-clientes-list")
    
class ClientesUpdateView(LoginRequiredMixin, UpdateView):
    model = Clientes
    success_url = reverse_lazy("proyecto-clientes-list")
    fields = ["nombre", "apellido", "dni", "edad",  "email", "imagen_viaj"]
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
    fields = ["nombre", "apellido", "dni", "edad",  "email", "imagen_viaj"]
    success_url = reverse_lazy("proyecto-proveedores-list")
    
class ProveedoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Proveedores
    success_url = reverse_lazy("proyecto-proveedores-list")
    fields = ["nombre", "apellido", "dni", "edad",  "email", "imagen_viaj"]
    template_name = "Appnuevo/proveedores_update.html"

class ProveedoresDeleteView(DeleteView):
    model = Proveedores
    success_url = reverse_lazy("proyecto-proveedores-list")
    template_name = "Appnuevo/proveedores_confirm_delete.html" 


#--------------------------------------------------------------------------------------------#

class DocumentacionList(LoginRequiredMixin, ListView):
    model = Documentacion
    template_name = "Appnuevo/documentacion_list.html"

class DocumentacionDetail(LoginRequiredMixin, DetailView):
    model = Documentacion
    template_name = "Appnuevo/documentacion_detail.html"
    
class DocumentacionCreate(LoginRequiredMixin, CreateView):
    model = Documentacion
    template_name = "Appnuevo/documentacion_create.html"
    fields = ["nombre", "fechatope", "entregado", "email", "imagen_viaj"]
    success_url = reverse_lazy("proyecto-documentacion-list")
    
class DocumentacionUpdate(LoginRequiredMixin, UpdateView):
    model = Documentacion
    success_url = reverse_lazy("proyecto-documentacion-list")
    fields = ["nombre", "fechatope", "entregado", "email", "imagen_viaj"]
    template_name = "Appnuevo/documentacion_update.html"
class DocumentacionDelete(DeleteView):
    model = Documentacion
    success_url = reverse_lazy("proyecto-documentacion-list")
    template_name = "Appnuevo/documentacion_confirm_delete.html"
        
