from django.urls import path 
from .views import index, cliente_create , lista_usuarios , cliente_update
app_name = 'cliente'
urlpatterns = [
    path('', index , name='index'),
  
    path('', lista_usuarios, name='index'),
    path('crear/', cliente_create, name='index'),
    path('actualizar/<int:pk>/', cliente_update, name='index'),
    ]
