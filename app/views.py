from django.shortcuts import render

# Create your views here.
def base(request):

    return render(request, 'app/base.html')

def inicio(request):

    return render(request, 'app/inicio.html')    

def productos(request):

    return render(request, 'app/productos.html')  

def servicios(request):

    return render(request, 'app/servicios.html')

def adm_clientes(request):

    return render(request, 'administradores/adm_clientes.html') 

def adm_productos(request):

    return render(request, 'administradores/adm_productos.html')   

def adm_servicios(request):

    return render(request, 'administradores/adm_servicios.html')   

def adm_trabajadores(request):

    return render(request, 'administradores/adm_trabajadores.html')   
