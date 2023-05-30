from django.shortcuts import render, redirect
from .form import ProductoForm
from .models import Producto

def index   (request) :
    return render(request, 'productos/index.html',)


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {'productos': productos})




def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:index')
    else:
        form = ProductoForm()
    return render(request, 'productos/crear-actualizar.html', {'form': form})

def producto_update(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos:index')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/crear-actualizar.html', {'form': form})