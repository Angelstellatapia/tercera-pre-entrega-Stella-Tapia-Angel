from django.urls import path
from .views import index, producto_create, producto_update, lista_productos
urlpatterns = [
    path('', index , name='index'),
    path('lista/', lista_productos, name='lista_productos'),
    path('crear/', producto_create, name='producto_create'),
    path('actualizar/<int:pk>/', producto_update, name='producto_update'),
]
