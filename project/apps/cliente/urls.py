from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='index'),
    path('crear/', views.cliente_create, name='crear'),
    path('actualizar/', views.cliente_update , name='actualizar'),
     
    ]
