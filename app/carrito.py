import cx_Oracle
from app.models import Producto

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")

        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
 
def agregar (self, Producto):
    id = str(Producto.id_producto)
    if id not in self.carrito.keys():
        self.carrito[id]={
            "id": Producto.id_producto,
            "nombre" : Producto.nombre,
            "total" : Producto.precio,
            "cantidad": 1,
        }
    else:
        self.carrito[id]["cantidad"]+=1
        self.carrito[id]["total"] += Producto.precio
    
    self.guardar_cart()

def guardar_cart (self):
    self.session["carrito"] = self.carrito
    self.session.modified = True

def eliminar(self, Producto):
    id = str(Producto.id_producto)
    if id in self.carrito:
        del self.carrito[id]
        self.guardar_cart()

def restar(self, Producto):
    id = str(Producto.id_producto)
    if id in self.carrito.keys():
        self.carrito[id]["cantidad"]-=1
        self.carrito[id]["total"]-=Producto.precio
        if self.carrito[id]["cantidad"] <= 0: self.eliminar(Producto)
        self.guardar_cart()

def limpiar(self):
    self.session["carrito"] = {}
    self.session.modified = True