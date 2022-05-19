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
        if i[3] is not None:
            data = {
                'data':i,
                'imagen':str(base64.b64encode(i[3].read()), 'utf-8')
            }
            lista.append(data)
        else:
            data = {
                'data':i,
                'imagen': None
            }
            lista.append(data)
    return lista

def listar_producto(id):
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("OBTENER_PRODUCTO", [id, out_cur])
    lista = []
    for i in out_cur:
        if i[3] is not None:
            data = {
                'data':i,
                'imagen':str(base64.b64encode(i[3].read()), 'utf-8')
            }
            lista.append(data)
        else:
            data = {
                'data':i,
                'imagen': None
            }
            lista.append(data)
    return lista

def agregar_producto(p_nombre, p_precio, p_imagen, p_stock, p_tp):
    cursor.callproc('INSERTAR_PRODUCTO', [p_nombre, p_precio, p_imagen, p_stock, p_tp])
    
def agregar_producto_sin_imagen(p_nombre, p_precio, p_stock, p_tp):
    cursor.callproc('INSERTAR_PRODUCTO_SIN_IMAGEN', [p_nombre, p_precio, p_stock, p_tp])

def modificar_producto(p_id_pro, p_nombre, p_precio, p_imagen, p_stock, p_tp):
    cursor.callproc('ACTUALIZAR_PRODUCTO', [p_id_pro, p_nombre, p_precio, p_imagen, p_stock, p_tp])
    
def modificar_producto_sin_imagen(p_id_pro, p_nombre, p_precio, p_stock, p_tp):
    cursor.callproc('ACTUALIZAR_PRODUCTO_SIN_IMAGEN', [p_id_pro, p_nombre, p_precio, p_stock, p_tp])

def modificar_producto(request, id):
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
        if 'pm_imagen' in request.FILES:
            pm_imagen = request.FILES['pm_imagen'].read()
            modificar_producto(id, pm_nombre, pm_precio, pm_imagen, pm_stock, pm_tp)
            return redirect(to="adm_productos")
        else:
            modificar_producto_sin_imagen(id, pm_nombre, pm_precio, pm_stock, pm_tp)
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
        if 'p_imagen' in request.FILES:
            p_imagen = request.FILES['p_imagen'].read()
            agregar_producto(p_nombre, p_precio, p_imagen, p_stock, p_tp); 
            data['productos'] = listado_productos() 
        else:
            agregar_producto_sin_imagen(p_nombre, p_precio, p_stock, p_tp);
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
