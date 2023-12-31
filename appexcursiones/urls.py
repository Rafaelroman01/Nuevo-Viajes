from django.urls import path
from appexcursiones.views import *
from appexcursiones import views
from django.contrib.auth.views import LogoutView
import Excursiones.settings as settings 
from django.conf.urls.static import static
import Excursiones.settings as settings 
from django.conf import settings 



urlpatterns = [
    path('inicio/', inicio, name="proyecto-inicio"),
    
    #path Viajes 
    path('viajes/list/', views.ViajesListViews.as_view(), name="proyecto-viajes-list"),
    path('viajes/detalle//<pk>/', views.ViajesDetailViews.as_view(), name="proyecto-viajes-detail"),
    path('viajes/crear/', views.ViajesCreateView.as_view(), name="proyecto-viajes-create"),
    path('viajes/actualizar/<pk>/', views.ViajesUpdateView.as_view(), name="proyecto-viajes-update"),
    path('viajes/borrar//<pk>/', views.ViajesDeleteView.as_view(), name="proyecto-viajes-delete"),
    
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

#Agregar las URLS de archivos estaticos
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    