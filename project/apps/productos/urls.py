from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='index'),
    path('crear/', views.producto_create, name='crear'),
    path('actualizar/', views.producto_update , name='actualizar'),
    
]
