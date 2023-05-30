
from django import forms
from cliente.models import cliente

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'        