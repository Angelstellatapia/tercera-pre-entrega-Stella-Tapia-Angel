from django.shortcuts import render
from cliente.models import cliente

# Create your views here.
def index   (request) :
    return render(request, 'cliente/index.html',)


def lista_usuarios(request):
    cliente_registrado = cliente.objects.all()
    return render(request, 'cliente/index.html.html', {'cliente':cliente_registrado})