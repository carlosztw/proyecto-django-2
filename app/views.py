from django.shortcuts import render, redirect
from django.db import connection
from django.core.paginator import Paginator
import base64
# Create your views here.
django_cursor = connection.cursor()
cursor = django_cursor.connection.cursor()

def base(request):
    return render(request, 'app/base.html')

def inicio(request):
    return render(request, 'app/inicio.html', {'index': 'active'})    

def navbar():
    aux = 'active'
    return aux

### CRUD PRODUCTOS ###
def productos(request):
    data = {
        'productos':listado_productos(),
        'prod': navbar()
    }    
    return render(request, 'app/productos.html', data)  

def listado_productos():
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("OBTENER_PRODUCTOS", [out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista

def listar_producto(id):
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("OBTENER_PRODUCTO", [id, out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista

def agregar_producto(p_nombre, p_precio, p_stock, p_tp, p_imagen):
    cursor.callproc('INSERTAR_PRODUCTO', [p_nombre, p_precio, p_stock, p_tp, p_imagen])
    
def modificar_producto(id, pm_nombre, pm_precio, pm_stock, pm_tp, pm_imagen):
    cursor.callproc('ACTUALIZAR_PRODUCTO', [id, pm_nombre, pm_precio, pm_stock, pm_tp, pm_imagen])
    
def adm_modificar_producto(request, id):
    data = {
        'producto':listar_producto(id),
        'a_p': navbar(),
        'categorias': listado_tipo_productos(),
    }
    if request.method == 'POST':
        pm_nombre = request.POST.get('pm_nombre')
        pm_precio = request.POST.get('pm_precio')
        pm_stock = request.POST.get('pm_stock')
        pm_tp = request.POST.get('pm_tp')
        pm_imagen = request.POST.get('pm_imagen')
        modificar_producto(id, pm_nombre, pm_precio, pm_stock, pm_tp, pm_imagen)
        return redirect(to="adm_productos")
    return render(request, 'administradores/adm_productos_modificar.html', data)

def eliminar_producto(request, id):
    cursor.callproc('ELIMINAR_PRODUCTO', [id])
    return redirect(to="adm_productos")

def adm_productos(request):
    data = {
        'productos':listado_productos(),
        'a_p': navbar(),
        'categorias': listado_tipo_productos(),
    }
    if request.method == 'POST':
        p_nombre = request.POST.get('p_nombre')
        p_precio = request.POST.get('p_precio')
        p_stock = request.POST.get('p_stock')
        p_tp = request.POST.get('p_tp')
        p_imagen = request.POST.get('p_imagen')
        agregar_producto(p_nombre, p_precio, p_stock, p_tp, p_imagen); 
        data['productos'] = listado_productos() 
    return render(request, 'administradores/adm_productos.html', data) 
  
def listado_tipo_productos():
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("LISTAR_TIPO_PRODUCTO", [out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista
### FIN CRUD PRODUCTOS ###


def servicios(request):
    return render(request, 'app/servicios.html', {'servicios': 'active'})

def adm_clientes(request):
    return render(request, 'administradores/adm_clientes.html', {'a_c': 'active'}) 

def adm_servicios(request):
    return render(request, 'administradores/adm_servicios.html', {'a_s': 'active'})   

def adm_trabajadores(request):
    return render(request, 'administradores/adm_trabajadores.html', {'a_t': 'active'})   
