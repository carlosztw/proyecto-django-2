class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get["carrito"]

        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

def agregar (self, producto):
    id = str(producto.id_producto)
    if id not in self.carrito.keys():
        self.carrito[id]={
            "id": producto.id_producto,
            "nombre" : producto.nombre,
            "total" : producto.precio,
            "cantidad": 1,
        }
    else:
        self.carrito[id]["cantidad"]+=1
        self.carrito[id]["total"] += producto.precio
    
    self.guardar_cart()

def guardar (self):
    self.session["carrito"] = self.carrito
    self.session.modified = True

def eliminar(self, producto):
    id = str(producto.id_producto)
    if id in self.carrito:
        del self.carrito[id]
        self.guardar_cart()

def restar(self, producto):
    id = str(producto.id_producto)
    if id in self.carrito.keys():
        self.carrito[id]["cantidad"]-=1
        self.carrito[id]["total"]-=producto.precio
        if self.carrito[id]["cantidad"] <= 0: self.eliminar_cart(producto)
        self.guardar_cart()

def limpiar(self):
    self.session["carrito"] = {}
    self.session.modified = True