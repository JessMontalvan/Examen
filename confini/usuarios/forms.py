from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta: 
        model = Usuario
        fields = [
            'nombre',
            'usuario',
            'contraseña',
            'edad',
            'telefono',
        ]

