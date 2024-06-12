from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Date Picker

class DateInput(forms.DateInput):
    input_type = 'date'


# - Register/Create a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# Login a user
        
class loginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a record

class CreateRecordForm(forms.ModelForm, DateInput):
    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'last_name_2', 'cedula', 'fecha_nacimiento', 'sexo', 'address', 'numero_record', 'nombre_padre', 'direccion_padre', 'nombre_madre', 'direccion_madre', 'nombre_conyuge', 'fecha', 'observaciones', 'email', 'phone', 'city', 'province', 'country']
        widgets = {
            'fecha': DateInput(),
            'fecha_nacimiento': DateInput()
        }

# - Update a record

class UpdateRecordForm(forms.ModelForm, DateInput):
    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'last_name_2', 'cedula', 'fecha_nacimiento', 'sexo', 'address', 'numero_record', 'nombre_padre', 'direccion_padre', 'nombre_madre', 'direccion_madre', 'nombre_conyuge', 'fecha', 'observaciones', 'email', 'phone', 'city', 'province', 'country']
        widgets = {
            'fecha': DateInput(),
            'fecha_nacimiento': DateInput()
        }   