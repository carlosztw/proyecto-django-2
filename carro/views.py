from django.shortcuts import render, redirect
from .carro import Carro
from app.models import Producto
# Create your views here.

### CARRO DE COMPRAS ###
def agregar_producto_carro(request, id_producto):
    carro=Carro(request)
    producto=Producto.objects.get(id_producto=id_producto)
    carro.agregar(Producto=producto)
    
    return redirect(request.META['HTTP_REFERER'])

def eliminar_producto_carro(request, id_producto):
    carro=Carro(request)
    producto=Producto.objects.get(id_producto=id_producto)
    carro.eliminar(Producto=producto)
    
    return redirect("carrito")

def restar_producto_carro(request, id_producto):
    carro=Carro(request)
    producto=Producto.objects.get(id_producto=id_producto)
    carro.restar_producto(Producto=producto)
    
    return redirect("carrito")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    
    return redirect("carrito")