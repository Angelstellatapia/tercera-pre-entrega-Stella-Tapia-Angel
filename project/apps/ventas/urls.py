from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='index'),
    path('crear/', views.pedido_create, name='crear'),
    path('actualizar/', views.pedido_update , name='actualizar'),
     
]
