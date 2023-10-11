from django.shortcuts import render, redirect
from django.http import HttpResponse
from appexcursiones.forms import ViajeFormulario, RecreadorFormulario, ClienteFormulario, ProveedorFormulario,  DocumentacionFormulario, UserRegisterForm,  UserEditForm
from appexcursiones.models import Viajes, Recreadores, Clientes, Proveedores, Documentacion   


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
    return render(request, "Appnuevo/inicio.html")
    
@login_required
def viajes(request):
    return render(request, "Appnuevo/viajes.html")

def creacion_viajes(request):
    #Validamos el tipo de peticion
    if request.method =="POST":
        formulario = ViajeFormulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            # Creamos los datos de los viajes
            viajes = Viajes(nombre=data["nombre"], destino=data["destino"], grupo=data["grupo"], email=data["email"])
            # Guardamos el formulario
            viajes.save()
    
    formulario = ViajeFormulario()
    contexto = {"formulario": formulario} 
    return render(request, "Appnuevo/viajes_formularios.html", contexto)

def buscar_viajes(request):
    return render(request, "Appnuevo/busqueda_viajes.html")

def resultados_buscar_viajes(request):
    nombre_viaje= request.GET["nombre_viaje"]
    viajes = Viajes.objects.filter(nombre__icontains=nombre_viaje)
    return render(request, "Appnuevo/resultados_busquedas_viajes.html", {"viajes":viajes})

def leer_viajes(request):
    #Trae todos los viajes
    viajes = Viajes.objects.all()
    contexto = {"viajes":viajes}
    return render(request, "Appnuevo/leerviajes.html", contexto)

def eliminar_viajes(request, id):
    #Trae todos los viajes
    viaje = Viajes.objects.get(id = id)
    viaje.delete()
    contexto = {"viaje": viaje}
    return render(request, "Appnuevo/viajes.html", contexto)


def editar_viajes(request, id):
    viaje = Viajes.objects.get(id = id)
    if request.method =="POST":
        formulario = ViajeFormulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            #
            viaje.nombre = data["nombre"]
            viaje.destino = data["destino"]
            viaje.grupo= data["grupo"]
            viaje.email= data["email"]
            # Guardamos el formulario
            viaje.save()
            return redirect("proyecto-documentacion-leer")
        else:
         return render(request, "Appnuevo/editar_curso.html", {"formulario":formulario, "errores": formulario.errors})
    else:
        formulario = ViajeFormulario(initial={"nombre":viaje.nombre, "grupo":viaje.grupo})
        return render(request, "Appnuevo/editar_curso.html",{"formulario":formulario, "errores": ""})


#def eliminar_curso(request, id):
    #Trae todos los viajes
    #viajes = Viajes.objects.get(id = id)
    #viajes.delete()
    
    #return redirect ("proyecto-viajes-borrar")


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

def test(request):
    ruta = os.path.join(BASE_DIR, "appexcursiones/templates/Appnuevo/base.html")
    print(BASE_DIR, __file__)
    file = open(ruta)
    return HttpResponse(file.read)
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
                return render(request, "Appnuevo/login.html", {"form": formulario, "errors": "Credenciales Invalidas"})
       
        else:
            return render(request, "Appnuevo/login.html", {"form": formulario, "errors": formulario.errors})
    formulario = AuthenticationForm()
    return render(request, "Appnuevo/login.html", {"form": formulario, "errors": errors})
    
def registrar_usuario(request):
    
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        
        if formulario.is_valid():
            
            formulario.save()
            return redirect("proyecto-inicio")
        else:
            return render(request, "Appnuevo/register.html", {"form": formulario, "errors": formulario.errors})
    
    formulario = UserRegisterForm()            
    return render(request, "Appnuevo/register.html", {"form": formulario})
        
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
            return render(request, "Appnuevo/editar_perfil.html", {"form": formulario, "erros": formulario.errors})
        
    else:
        #Crear el formulario vacio 
        formulario = UserEditForm(initial={"email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name})
        
    return render(request, "Appnuevo/editar_perfil.html", {"form": formulario})

