
from django import forms
from .models import Usuario

class clienteForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'direccion', 'telefono'] 