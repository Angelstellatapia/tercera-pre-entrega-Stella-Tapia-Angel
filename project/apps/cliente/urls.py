from django.urls import path 
from .views import index, cliente_create , lista_usuarios , cliente_update
urlpatterns = [
    path('', index , name='index'),
  
    path('lista/', lista_usuarios, name='index'),
    path('crear/', cliente_create, name='index'),
    path('actualizar/<int:pk>/', cliente_update, name='index'),
    ]
