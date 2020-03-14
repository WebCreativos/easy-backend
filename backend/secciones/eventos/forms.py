from django import forms
from .models import Usuarios


class usuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['email', 'celular', 'nombre', 'apellido']


