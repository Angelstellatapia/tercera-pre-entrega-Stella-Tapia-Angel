from django.urls import path 
from .views import index, cliente_create , lista_usuarios , cliente_update
urlpatterns = [
    path('', index , name='index'),
  
    path('lista/', lista_usuarios, name='index'),
    path('crear/', cliente_create, name='crear-actualizar'),
    path('actualizar/<int:pk>/', cliente_update, name='crear-actualizar'),
    ]
