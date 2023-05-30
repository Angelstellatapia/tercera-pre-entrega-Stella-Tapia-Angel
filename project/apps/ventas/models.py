#from django.db import models

#from cliente.models import cliente
#from productos.models import Producto
#
#class Pedido(models.Model):
#    usuario = models.ForeignKey(cliente, on_delete=models.CASCADE)
#    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#    cantidad = models.IntegerField()
#    fecha = models.DateField(auto_now_add=True)
#
#    def __str__(self):
#        return f"Pedido de {self.cliente} - {self.producto}"
from django.db import models

class Pedido(models.Model):
    cliente = models.ForeignKey('cliente.Usuario', on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"Pedido de {self.producto} para {self.cliente}"