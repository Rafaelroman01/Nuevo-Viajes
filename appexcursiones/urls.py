from django.urls import path
from appexcursiones.views import *
from appexcursiones import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio, name="proyecto-inicio"),
    #path Viajes 
    path('viajes/', viajes, name="proyecto-viajes"),
    path('viajes/actualizar/<id>/', editar_viajes, name="proyecto-viajes-editar"),
    path('viajes/borrar/<id>/', eliminar_viajes, name="proyecto-viajes-borrar"),
    path('viajes/buscar/', buscar_viajes, name="proyecto-viajes-buscar"),
    path('viajes/buscar/resultados/', resultados_buscar_viajes, name="proyecto-viajes-buscar-resultados"),
    
    
    path('clientes/', clientes, name="proyecto-clientes"),
    path('clientes/crear/',creacion_clientes, name="proyecto-clientes-crear"),
    path('proveedores/', proveedores, name="proyecto-proveedores"),
    path('proveedores/crear/', creacion_proveedores, name="proyecto-proveedores-crear"),
    path('clientes/leer/', leer_clientes, name="proyecto-clientes-leer"),
    path('proveedores/leer/', leer_proveedores, name="proyecto-proveedores-leer"),
    
    #Recreadores
    path('recreadores/list/', views.RecreadoresListViews.as_view(), name="proyecto-recreadores-list"),
    path('recreadores/detalle//<pk>/', views.RecreadoresDetailViews.as_view(), name="proyecto-recreadores-detail"),
    path('recreadores/crear/', views.RecreadoresCreateView.as_view(), name="proyecto-recreadores-create"),
    path('recreadores/actualizar/<pk>/', views.RecreadoresUpdateView.as_view(), name="proyecto-recreadores-update"),
    path('recreadores/borrar//<pk>/', views.RecreadoresDeleteView.as_view(), name="proyecto-recreadores-delete"),
    
    #Documentacion
    #path('documentacion', documentacion, name="proyecto-documentacion"),
    path('documentacion/list',  views.DocumentacionList.as_view(), name="proyecto-documentacion-list"),
    path('documentacion/detail//<pk>/',  views.DocumentacionDetail.as_view(), name="proyecto-documentacion-detail"),
    path('documentacion/create/',  views.DocumentacionCreate.as_view(), name="proyecto-documentacion-create"),
    path('documentacion/update/<pk>/',  views.DocumentacionUpdate.as_view(), name="proyecto-documentacion-update"),
    path('documentacion/delete//<pk>/',  views.DocumentacionDelete.as_view(), name="proyecto-documentacion-delete"),
    
    
]