from django.urls import path
from authentication_app.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('about/', prueba_app, name="app-prueba"),
    path('salida/', prueba_salida, name="app-salida"),
]