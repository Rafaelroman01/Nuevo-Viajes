from django.urls import path
from authentication_app.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('about/', prueba_app, name="appdos-conoceme"),
    
    ## Login ##
    
    path('test/', test),
    path('login/', iniciar_sesion, name="auth-login"),
    path('register/', registrar_usuario, name="auth-register"),
    path('logout/', LogoutView.as_view(template_name="Appnuevo/logout.html"), name="auth-logout"),
    path('perfil/editar/', editar_perfil, name="auth-editar-perfil"),
    path('perfil/avatar/', agregar_avatar, name="auth-avatar"),
    
]