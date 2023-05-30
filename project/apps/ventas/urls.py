from django.urls import path
from .views import index, pedido_create, pedido_list, pedido_update
urlpatterns = [
    path('', index , name='index'),
    path('lista/', pedido_list, name='index'),
    path('crear/', pedido_create, name='index'),
    path('actualizar/<int:pk>/', pedido_update, name='index'),
]
