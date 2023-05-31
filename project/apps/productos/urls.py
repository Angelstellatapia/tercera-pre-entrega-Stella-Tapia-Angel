from django.urls import path
from .views import index, producto_create, producto_update, lista_productos
urlpatterns = [
    path('', index , name='index'),
    path('lista/', lista_productos, name='index'),
    path('crear/', producto_create, name='index'),
    path('actualizar/<int:pk>/', producto_update, name='index'),
]
