from django.db import models

#from cliente.models import cliente#

##class Producto(models.Model):
#    nombre = models.CharField(max_length=100)
#    descripcion = models.TextField()
#    precio = models.DecimalField(max_digits=10, decimal_places=2)
#    propietario = models.ForeignKey(cliente, on_delete=models.CASCADE)#

#    def __str__(self):
#        return self.nombre
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre