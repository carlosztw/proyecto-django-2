from django.shortcuts import render
from django.db import connection
# Create your views here.
def base(request):

    return render(request, 'app/base.html')

def inicio(request):

    return render(request, 'app/inicio.html', {'index': 'active'})    

def navbar():
    aux = 'active'
    return aux

### PRODUCTOS CRUD ###
def productos(request):
    data = {
        'productos':listado_productos(),
        'prod': navbar()
    }

    return render(request, 'app/productos.html', data)  

def listado_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("OBTENER_PRODUCTOS", [out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista

def listado_tipo_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LISTAR_TIPO_PRODUCTO", [out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista

def adm_productos(request):
    data = {
        'productos':listado_productos(),
        'a_p': navbar(),
        'categorias': listado_tipo_productos()
    }
    return render(request, 'administradores/adm_productos.html', data) 

### FIN CRUD PRODUCTOS ###



def servicios(request):

    return render(request, 'app/servicios.html', {'servicios': 'active'})

def adm_clientes(request):

    return render(request, 'administradores/adm_clientes.html', {'a_c': 'active'}) 

def adm_servicios(request):

    return render(request, 'administradores/adm_servicios.html', {'a_s': 'active'})   

def adm_trabajadores(request):

    return render(request, 'administradores/adm_trabajadores.html', {'a_t': 'active'})   
