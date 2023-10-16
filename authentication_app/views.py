from django.shortcuts import render, redirect
from django.http import HttpResponse
from appexcursiones.forms import ViajeFormulario, RecreadorFormulario, ClienteFormulario, ProveedorFormulario,  DocumentacionFormulario, UserRegisterForm,  UserEditForm, AvatarForm
from appexcursiones.models import Viajes, Recreadores, Clientes, Proveedores, Documentacion, Avatar   

from django.shortcuts import render
from django.http import HttpResponse


#Dependencia para resolver apertura de archivos usando rutas relativas
from Excursiones.settings import BASE_DIR
import os



# Creacion de Clases basados en vistas

# login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def prueba_app(request):
    return render(request, "Appdos/acercaDeMi.html")

def test(request):
    ruta = os.path.join(BASE_DIR, "appexcursiones/templates/Appnuevo/base.html")
    print(BASE_DIR, __file__)
    file = open(ruta)
    return HttpResponse(file.read)

def iniciar_sesion(request):
    errors = ""
    if request.method =="POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            user = authenticate(username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                return redirect("proyecto-inicio")
            else:
                return render(request, "Appdos/login.html", {"form": formulario, "errors": "Credenciales Invalidas"})
       
        else:
            return render(request, "Appdos/login.html", {"form": formulario, "errors": formulario.errors})
    formulario = AuthenticationForm()
    return render(request, "Appdos/login.html", {"form": formulario, "errors": errors})
    
def registrar_usuario(request):
    
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        
        if formulario.is_valid():
            
            formulario.save()
            return redirect("proyecto-inicio")
        else:
            return render(request, "Appdos/register.html", {"form": formulario, "errors": formulario.errors})
    
    formulario = UserRegisterForm()            
    return render(request, "Appdos/register.html", {"form": formulario})

@login_required       
def editar_perfil(request):
    
    usuario = request.user
    
    if request.method == "POST":
        # Cargar informacion en el formulario
        formulario = UserEditForm(request.POST)
        
        #Validacion del formulario
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            #Actualizacion del usuario con los datos del formulario
            
            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            
            usuario.save()
            return redirect("proyecto-inicio")
        else:
            return render(request, "Appdos/editar_perfil.html", {"form": formulario, "erros": formulario.errors})
        
    else:
        #Crear el formulario vacio 
        formulario = UserEditForm(initial={"email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name})
        
    return render(request, "Appdos/editar_perfil.html", {"form": formulario})


@login_required
def agregar_avatar(request):
    if request.method =="POST":
        formulario = AvatarForm(request.POST, files= request.FILES)
        print(request.FILES, request.POST )
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            usuario = request.user 
            avatar = Avatar (user=usuario, imagen=data["imagen"])
            avatar.save()
            return redirect("proyecto-inicio")
        else:
            return render(request, "Appdos/agregar_avatar.html", {"form": formulario, "errors": formulario.errors})
    formulario = AvatarForm()
    return render(request, "Appdos/agregar_avatar.html", {"form": formulario})


