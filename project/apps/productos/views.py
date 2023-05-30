from django.shortcuts import render
from .models import Producto
def index   (request) :
    return render(request, 'productos/index.html',)


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {'productos': productos})