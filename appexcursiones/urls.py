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
    
     #path Recreadores
    path('recreadores/list/', views.RecreadoresListViews.as_view(), name="proyecto-recreadores-list"),
    path('recreadores/detalle//<pk>/', views.RecreadoresDetailViews.as_view(), name="proyecto-recreadores-detail"),
    path('recreadores/crear/', views.RecreadoresCreateView.as_view(), name="proyecto-recreadores-create"),
    path('recreadores/actualizar/<pk>/', views.RecreadoresUpdateView.as_view(), name="proyecto-recreadores-update"),
    path('recreadores/borrar//<pk>/', views.RecreadoresDeleteView.as_view(), name="proyecto-recreadores-delete"),
    
     #path Clientes
    path('clientes/list/', views.ClientesListViews.as_view(), name="proyecto-clientes-list"),
    path('clientes/detalle//<pk>/', views.ClientesDetailViews.as_view(), name="proyecto-clientes-detail"),
    path('clientes/crear/', views.ClientesCreateView.as_view(), name="proyecto-clientes-create"),
    path('clientes/actualizar/<pk>/', views.ClientesUpdateView.as_view(), name="proyecto-clientes-update"),
    path('clientes/borrar//<pk>/', views.ClientesDeleteView.as_view(), name="proyecto-clientes-delete"),
    
    
     #path Proveedores
    path('proveedores/list/', views.ProveedoresListViews.as_view(), name="proyecto-proveedores-list"),
    path('proveedores/detalle//<pk>/', views.ProveedoresDetailViews.as_view(), name="proyecto-proveedores-detail"),
    path('proveedores/crear/', views.ProveedoresCreateView.as_view(), name="proyecto-proveedores-create"),
    path('proveedores/actualizar/<pk>/', views.ProveedoresUpdateView.as_view(), name="proyecto-proveedores-update"),
    path('proveedores/borrar//<pk>/', views.ProveedoresDeleteView.as_view(), name="proyecto-proveedores-delete"),
   
    
    #path Documentacion
    path('documentacion/list',  views.DocumentacionList.as_view(), name="proyecto-documentacion-list"),
    path('documentacion/detail//<pk>/',  views.DocumentacionDetail.as_view(), name="proyecto-documentacion-detail"),
    path('documentacion/create/',  views.DocumentacionCreate.as_view(), name="proyecto-documentacion-create"),
    path('documentacion/update/<pk>/',  views.DocumentacionUpdate.as_view(), name="proyecto-documentacion-update"),
    path('documentacion/delete//<pk>/',  views.DocumentacionDelete.as_view(), name="proyecto-documentacion-delete"),
    
    
]