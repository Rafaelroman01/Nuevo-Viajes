from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ViajeFormulario(forms.Form):
    nombre= forms.CharField(max_length=50)
    destino= forms.CharField(max_length=50)
    grupo = forms.IntegerField()
    email= forms.EmailField(max_length=80)
    imagen_viaj= forms.ImageField()
    
#class RecreadorFormulario(forms.Form):
    #nombre = forms.CharField(max_length=50)
    #apellido = forms.CharField(max_length=50)
    #dni = forms.IntegerField()
    #edad = forms.IntegerField()
    #email= forms.EmailField(max_length=80)
  
#class ClienteFormulario(forms.Form):
    #nombre = forms.CharField(max_length=50)
    #apellido = forms.CharField(max_length=50)
    #dni = forms.IntegerField()
    #edad = forms.IntegerField()
    #email= forms.EmailField(max_length=80)
   
#class ProveedorFormulario(forms.Form):
    #nombre = forms.CharField(max_length=50)
    #apellido = forms.CharField(max_length=50)
    #dni = forms.IntegerField()
    #edad = forms.IntegerField()
    #email= forms.EmailField(max_length=80) 


class UserRegisterForm(UserCreationForm):
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    email= forms.EmailField(label="Correo Electronico")
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme el password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =["username", "email", "last_name", "first_name", "password1", "password2" ] 
    
class UserEditForm(UserCreationForm):
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    email= forms.EmailField(label="Correo Electronico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)
    password1 = forms.CharField(label="Confirme el Password", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields =[ "email", "last_name", "first_name"] 
        #Elimina cualquier mensaje de ayuda en los campos
        help_texts = {"email": "Indica un correo electronico que uses habitualmente", "first_name": "" , "last_name": ""}
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField()