from django.shortcuts import render, redirect
from cliente.models import cliente
from cliente.form import clienteForm

# Create your views here.
def index   (request) :
    return render(request, 'cliente/index.html',)


def lista_usuarios(request):
    cliente_registrado = cliente.objects.all()
    return render(request, 'cliente/index.html', {'cliente':cliente_registrado})

def cliente_create(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente:index')
    else:
        form = clienteForm()
    return render(request, 'cliente/crear-actualizar.html', {'form': form})

def cliente_update(request, pk):
    usuario = cliente.objects.get(pk=pk)
    if request.method == 'POST':
        form = clienteForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('cliente:index')
    else:
        form = clienteForm(instance=usuario)
    return render(request, 'cliente/crear-actualizar.html', {'form': form})