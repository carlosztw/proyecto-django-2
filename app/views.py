from django.shortcuts import render
from django.db import connection
# Create your views here.
def base(request):

    return render(request, 'app/base.html')

def inicio(request):

    return render(request, 'app/inicio.html', {'index': 'active'})    

### PRODUCTOS CRUD ###
def productos(request):

    return render(request, 'app/productos.html', {'productos': 'active'})  





def servicios(request):

    return render(request, 'app/servicios.html', {'servicios': 'active'})

def adm_clientes(request):

    return render(request, 'administradores/adm_clientes.html', {'a_c': 'active'}) 

def adm_productos(request):

    return render(request, 'administradores/adm_productos.html', {'a_p': 'active'})   

def adm_servicios(request):

    return render(request, 'administradores/adm_servicios.html', {'a_s': 'active'})   

def adm_trabajadores(request):

    return render(request, 'administradores/adm_trabajadores.html', {'a_t': 'active'})   
