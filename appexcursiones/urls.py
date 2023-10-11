from django.urls import path
from appexcursiones.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio, name="proyecto-inicio"),
    path('viajes/', viajes, name="proyecto-viajes"),
    path('viajes/crear/', creacion_viajes, name="proyecto-viajes-crear"),
    path('viajes/buscar/', buscar_viajes, name="proyecto-viajes-buscar"),
    path('viajes/buscar/resultados/', resultados_buscar_viajes, name="proyecto-viajes-buscar-resultados"),
    path('recreadores/', recreadores, name="proyecto-recreadores"),
    path('recreadores/crear/', creacion_recreadores, name="proyecto-recreadores-crear"),
    path('clientes/', clientes, name="proyecto-clientes"),
    path('clientes/crear/',creacion_clientes, name="proyecto-clientes-crear"),
    path('proveedores/', proveedores, name="proyecto-proveedores"),
    path('proveedores/crear/', creacion_proveedores, name="proyecto-proveedores-crear"),
    path('viajes/leer/', leer_viajes, name="proyecto-viajes-leer"),
    path('recreadores/leer/', leer_recreadores, name="proyecto-recreadores-leer"),
    path('clientes/leer/', leer_clientes, name="proyecto-clientes-leer"),
    path('proveedores/leer/', leer_proveedores, name="proyecto-proveedores-leer"),
    path('viajes/borrar/<id>/', eliminar_viajes, name="proyecto-viajes-borrar"),
    path('viajes/actualizar/<id>/', editar_viajes, name="proyecto-viajes-editar"),
    
    
    
    path('documentacion/', DocumentacionList.as_view(), name="proyecto-documentacion"),
    path('documentacion/detalle/<pk>/', DocumentacionDetail.as_view(), name="proyecto-documentacion-detail"),
    path('documentacion/crear/', DocumentacionCreate.as_view(), name="proyecto-documentacion-create"),
    path('documentacion/actualizar/<pk>/', DocumentacionUpdate.as_view(), name="proyecto-documentacion-update"),
    path('documentacion/borrar/<pk>/', DocumentacionDelete.as_view(), name="proyecto-documentacion-delete"),
    
    # Login
    path('test/', test),
    path('login/', iniciar_sesion, name="auth-login"),
    path('register/', registrar_usuario, name="auth-register"),
    path('logout/', LogoutView.as_view(template_name="Appnuevo/logout.html"), name="auth-logout"),
    path('perfil/editar/', editar_perfil, name="auth-editar-perfil"),
    path('perfil/avatar/', agregar_avatar, name="auth-avatar"),
]