from django.shortcuts import render, redirect
from ventas.models import Pedido
from ventas.form import PedidoForm

# Create your views here.
def index   (request) :
    return render(request, 'ventas/index.html',)



def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'ventas/index.html', {'pedidos': pedidos})

def pedido_create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido:index')
    else:
        form = PedidoForm()
    return render(request, 'ventas/crear-actualizar.html', {'form': form})

def pedido_update(request, pk):
    pedido = Pedido.objects.get(pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pedido:index')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'ventas/crear-actualizar.html', {'form': form})