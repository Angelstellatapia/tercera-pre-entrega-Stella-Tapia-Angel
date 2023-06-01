from django.shortcuts import render, redirect
from .models import Usuario
from .form import clienteForm

# Create your views here.
def index   (request) :
    return render(request, 'cliente/index.html',)


def lista_usuarios(request):
    usuario= Usuario.objects.all()
    return render(request, 'cliente/index.html', {'Usuario':usuario})

def cliente_create(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente:index')
    else:
        form = clienteForm()
    return render(request, 'cliente/index.html', {'form': form})

def cliente_update(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        form = clienteForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('cliente:index')
    else:
        form = clienteForm(instance=usuario)
    return render(request, 'cliente/index.html', {'form': form})