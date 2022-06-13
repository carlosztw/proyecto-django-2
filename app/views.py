import email
from django.shortcuts import render, redirect
from django.db import connection
from django.core.paginator import Paginator
from django.http import Http404
import cx_Oracle
#importar el modelo de la tabla user
from django.contrib.auth.models import User
#importar libreria para autentificar usuarios 
from django.contrib.auth import authenticate,logout,login as login_aut
#importar libreria decoradora que evita el ingreso a las paginas 
from django.contrib.auth.decorators import login_required



# Create your views here.
django_cursor = connection.cursor()
cursor = django_cursor.connection.cursor()

def base(request):
    return render(request, 'app/base.html')

def inicio(request):
    return render(request, 'app/inicio.html')    

def navbar():
    aux = 'active'
    return aux

### CRUD PRODUCTOS ###
def productos(request):
    listadoProductos = listado_productos()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(listadoProductos, 9)
        listadoProductos = paginator.page(page)
    except:
        raise Http404
    data = {
        'productos':listadoProductos,
        'paginator': paginator,  
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
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('INSERTAR_PRODUCTO', [p_nombre, p_precio, p_stock, p_tp, p_imagen, salida])
    return salida.getvalue()
    
def modificar_producto(id, pm_nombre, pm_precio, pm_stock, pm_tp, pm_imagen):
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_PRODUCTO', [id, pm_nombre, pm_precio, pm_stock, pm_tp, pm_imagen, salida])
    return salida.getvalue()

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
        salida = modificar_producto(id, pm_nombre, pm_precio, pm_stock, pm_tp, pm_imagen)
        if salida == 1:
            data['mensaje'] = "Producto modificado"
        else:
            data['mensajeError'] = 'El producto no fue modificado' 
        return redirect(to="adm_productos")
    return render(request, 'administradores/adm_productos_modificar.html', data)

def eliminar_producto(request, id):
    cursor.callproc('ELIMINAR_PRODUCTO', [id])
    return redirect(to="adm_productos")

def adm_productos(request):
    listadoProductos = listado_productos()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(listadoProductos, 9)
        listadoProductos = paginator.page(page)
    except:
        raise Http404

    data = {
        'productos':listadoProductos,
        'paginator': paginator,
        'a_p': navbar(),
        'categorias': listado_tipo_productos(),
    }
    if request.method == 'POST':
        p_nombre = request.POST.get('p_nombre')
        p_precio = request.POST.get('p_precio')
        p_stock = request.POST.get('p_stock')
        p_tp = request.POST.get('p_tp')
        p_imagen = request.POST.get('p_imagen')
        salida = agregar_producto(p_nombre, p_precio, p_stock, p_tp, p_imagen);
        if salida == 1:
            data['mensaje'] = "Producto agregado"
        else:
            data['mensajeError'] = 'El producto no fue agregado' 
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

### CRUD TRABJADORES ###
def listado_trabajadores():
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("OBTENER_TRABAJADORES", [out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista

def listar_trabajador(id):
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("OBTENER_TRABAJADOR", [id, out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista

def agregar_trabajador(t_rut, t_dv, t_pn, t_sn, t_pa, t_sa, t_c, t_p, t_d, t_te, t_s, t_nc, t_temp, t_b, t_tc):
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('INSERTAR_TRABAJADOR', [t_rut, t_dv, t_pn, t_sn, t_pa, t_sa, t_c, t_p, t_d, t_te, t_s, t_nc, t_temp, t_b, t_tc, salida])
    return salida.getvalue()

def modificar_trabajador(id, t_pn, t_sn, t_pa, t_sa, t_c, t_p, t_d, t_te, t_s, t_nc, t_temp, t_b, t_tc):
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('MODIFICAR_TRABAJADOR', [id, t_pn, t_sn, t_pa, t_sa, t_c, t_p, t_d, t_te, t_s, t_nc, t_temp, t_b, t_tc, salida])
    return salida.getvalue()

def adm_trabajadores(request):
    data = {
        'a_t': 'active',
        't_empleado': listado_tipo_empleado(),
        'bancos': listado_banco(),
        't_cuenta': listado_tipo_cuenta(),
        'trabajadores': listado_trabajadores()
    }
    if request.method == 'POST':
        t_rut = request.POST.get('t_rut')
        t_dv = request.POST.get('t_dv')
        t_pn = request.POST.get('t_pn')
        t_sn = request.POST.get('t_sn')
        t_pa = request.POST.get('t_pa')
        t_sa = request.POST.get('t_sa')
        t_c = request.POST.get('t_c')
        t_p = request.POST.get('t_p')
        t_d = request.POST.get('t_d')
        t_te = request.POST.get('t_te')
        t_s = request.POST.get('t_s')
        t_nc = request.POST.get('t_nc')
        t_temp = request.POST.get('t_temp')
        t_b = request.POST.get('t_b')
        t_tc = request.POST.get('t_tc')
        salida = agregar_trabajador(t_rut, t_dv, t_pn, t_sn, t_pa, t_sa, t_c, t_p, t_d, t_te, t_s, t_nc, t_temp, t_b, t_tc); 
        if salida == 1:
            data['mensaje'] = 'Trabajador agregado'
        else:   
            data['mensajeError'] = 'El trabajador no fue agregado'
        data['trabajadores'] = listado_trabajadores() 
    return render(request, 'administradores/adm_trabajadores.html', data)   

def adm_modificar_trabajadores(request, id):
    data = {
        'a_t': 'active',
        't_empleado': listado_tipo_empleado(),
        'bancos': listado_banco(),
        't_cuenta': listado_tipo_cuenta(),
        'trabajador': listar_trabajador(id)
    }
    if request.method == 'POST':
        tm_pn = request.POST.get('tm_pn')
        tm_sn = request.POST.get('tm_sn')
        tm_pa = request.POST.get('tm_pa')
        tm_sa = request.POST.get('tm_sa')
        tm_c = request.POST.get('tm_c')
        tm_p = request.POST.get('tm_p')
        tm_d = request.POST.get('tm_d')
        tm_te = request.POST.get('tm_te')
        tm_s = request.POST.get('tm_s')
        tm_nc = request.POST.get('tm_nc')
        tm_temp = request.POST.get('tm_temp')
        tm_b = request.POST.get('tm_b')
        tm_tc = request.POST.get('tm_tc')
        salida = modificar_trabajador(id, tm_pn, tm_sn, tm_pa, tm_sa, tm_c, tm_p, tm_d, tm_te, tm_s, tm_nc, tm_temp, tm_b, tm_tc); 
        if salida == 1:
            data['mensaje'] = "Trabajador modificado"
        else:
            data['mensajeError'] = 'El trabajador no fue modificado' 
        return redirect(to="adm_trabajadores")
    return render(request, 'administradores/adm_trabajadores_modificar.html', data)   

def eliminar_trabajador(request, id):
    cursor.callproc('ELIMINAR_TRABAJADOR', [id])
    return redirect(to="adm_trabajadores")

def listado_tipo_empleado():
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("LISTAR_TIPO_EMPLEADO", [out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista

def listado_banco():
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("LISTAR_BANCO", [out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista

def listado_tipo_cuenta():
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("LISTAR_TIPO_CUENTA", [out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista
### FIN CRUD TRABAJADORES ###

### CRUD CLIENTES ###
def listado_clientes():
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("OBTENER_CLIENTES", [out_cur])
    
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista

def listar_cliente(id):
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("OBTENER_CLIENTE", [id, out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista

def agregar_cliente(c_rut, c_dv, c_pn, c_sn, c_pa, c_sa, c_c, c_p, c_d, c_te):
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('INSERTAR_CLIENTE', [c_rut, c_dv, c_pn, c_sn, c_pa, c_sa, c_c, c_p, c_d, c_te, salida])
    return salida.getvalue()

def modificar_cliente(id, c_rut, c_dv, c_pn, c_sn, c_pa, c_sa, c_c, c_p, c_d, c_te):
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('MODIFICAR_CLIENTE', [id, c_rut, c_dv, c_pn, c_sn, c_pa, c_sa, c_c, c_p, c_d, c_te, salida])
    return salida.getvalue()

def adm_clientes(request):
    data = {
        'clientes':listado_clientes(),
        'clie': navbar()
    }
    if request.method == 'POST':
        c_rut = request.POST.get('c_rut')
        c_dv = request.POST.get('c_dv')
        c_pn = request.POST.get('c_pn')
        c_sn = request.POST.get('c_sn')
        c_pa = request.POST.get('c_pa')
        c_sa = request.POST.get('c_sa')
        c_c = request.POST.get('c_c')
        c_p = request.POST.get('c_p')
        c_d = request.POST.get('c_d')
        c_te = request.POST.get('c_te')
        salida = agregar_cliente(c_rut, c_dv, c_pn, c_sn, c_pa, c_sa, c_c, c_p, c_d, c_te); 
        if salida == 1:
            data['mensaje'] = 'Cliente agregado'
        else:   
            data['mensajeError'] = 'El cliente no fue agregado'
        data['clientes'] = listado_clientes() 
    return render(request, 'administradores/adm_clientes.html', data)   

def adm_modificar_clientes(request, id):
    data = {
        'a_c': 'active',
        'cliente': listar_cliente(id)
    }
    if request.method == 'POST':
        cm_rut = request.POST.get('cm_rut')
        cm_dv = request.POST.get('cm_dv')
        cm_pn = request.POST.get('cm_pn')
        cm_sn = request.POST.get('cm_sn')
        cm_pa = request.POST.get('cm_pa')
        cm_sa = request.POST.get('cm_sa')
        cm_c = request.POST.get('cm_c')
        cm_p = request.POST.get('cm_p')
        cm_d = request.POST.get('cm_d')
        cm_te = request.POST.get('cm_te')
        salida = modificar_cliente(id, cm_rut, cm_dv, cm_pn, cm_sn, cm_pa, cm_sa, cm_c, cm_p, cm_d, cm_te); 
        if salida == 1:
            data['mensaje'] = "Cliente modificado"
        else:
            data['mensajeError'] = 'El Cliente no fue modificado' 
        return redirect(to="adm_clientes")
    return render(request, 'administradores/adm_clientes_modificar.html', data)   

def eliminar_cliente(request, id):
    cursor.callproc('ELIMINAR_CLIENTE', [id])
    return redirect(to="adm_clientes")


### FIN CRUD CLIENTES ###

def servicios(request):
    return render(request, 'app/servicios.html', {'servicios': 'active'})

def adm_servicios(request):
    return render(request, 'administradores/adm_servicios.html', {'a_s': 'active'})   

def registroC(request):
    data = {}
    if request.method == 'POST':
        c_rut = request.POST.get('txtrut')
        c_dv = request.POST.get('txtRuv')
        c_pn = request.POST.get('txtNombre')
        c_sn = request.POST.get('txtsegNombre')
        c_pa = request.POST.get('txtapellido_pa')
        c_sa = request.POST.get('txtapellido_ma')
        c_c = request.POST.get('txtCorreo')
        c_p = request.POST.get('txtcontrasena')
        c_d = request.POST.get('txtDireccion')
        c_te = request.POST.get('txtNumero')
        salida = agregar_cliente(c_rut, c_dv, c_pn, c_sn, c_pa, c_sa, c_c, c_p, c_d, c_te); 
        if salida == 1:
            data['mensaje'] = 'Cliente agregado'
        else:   
            data['mensajeError'] = 'El cliente no fue agregado'
        data['clientes'] = listado_clientes() 








    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido_pa = request.POST.get("txtapellido_pa")
        email = request.POST.get("txtCorreo")
        nom_usuario = request.POST.get("txtUsuario")
        pass1 = request.POST.get("txtcontrasena")

        usu = User()
        usu.first_name = nombre
        usu.last_name = apellido_pa
        usu.username = nom_usuario
        usu.set_password(pass1)
        usu.save

    return render(request, 'app/registroC.html', {'registroC': 'active'})


def cerrar_sesion(request):
    logout(request)
    return render(request, 'app/inicio.html')


def login(request):
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtUsuario")
        contra = request.POST.get("txtcontrasena")
        us = authenticate(request,username=nombre,password=contra)
        if us is not None and us.is_active:
            login_aut(request,us)
            return render(request, 'app/inicio.html')
        else:
            mensaje="no existe usuario o contra incorrecta"
    contexto={"mensaje":mensaje}            
    return render(request, 'app/login.html', contexto)    

