from django.shortcuts import render, redirect
from django.db import connection
from django.core.paginator import Page, Paginator
from django.http import Http404
from django.core.files.storage import FileSystemStorage
import cx_Oracle
#importar el modelo de la tabla user
from django.contrib.auth.models import User, Group
#importar libreria para autentificar usuarios 
from django.contrib.auth import authenticate,logout,login as login_aut
#importar libreria decoradora que evita el ingreso a las paginas 
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
django_cursor = connection.cursor()
cursor = django_cursor.connection.cursor()

group_vendedor = Group.objects.get(name='vendedor')
group_adm = Group.objects.get(name='administrador')
group_tecnico = Group.objects.get(name='tecnico')

def base(request):
    return render(request, 'app/base.html')

def inicio(request):
    data={
        'index': navbar()
    }
    return render(request, 'app/inicio.html', data)    

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


@permission_required('app.change_producto')
def adm_modificar_producto(request, id):    
    data = {
        'producto':listar_producto(id),
        'a_p': navbar(),
        'categorias': listado_tipo_productos(),
    }
    if request.method == 'POST' and bool(request.FILES.get('pm_imagen', False)) == True:
        pm_nombre = request.POST.get('pm_nombre')
        pm_precio = request.POST.get('pm_precio')
        pm_stock = request.POST.get('pm_stock')
        pm_tp = request.POST.get('pm_tp')
        pm_imagen = request.FILES['pm_imagen']
        fs = FileSystemStorage()
        filename = fs.save(pm_imagen.name, pm_imagen)
        uploaded_file_url = fs.url(filename)
        salida = modificar_producto(id, pm_nombre, pm_precio, pm_stock, pm_tp, uploaded_file_url);
    else:
        pm_nombre = request.POST.get('pm_nombre')
        pm_precio = request.POST.get('pm_precio')
        pm_stock = request.POST.get('pm_stock')
        pm_tp = request.POST.get('pm_tp')
        pm_imagen = None
        salida = modificar_producto(id, pm_nombre, pm_precio, pm_stock, pm_tp, pm_imagen);

    if salida == 1:
        data['mensaje'] = "Producto modificado"
        return redirect(to="adm_productos")
    elif salida == 0:
        data['mensaje'] = 'El producto no fue modificado' 
    return render(request, 'administradores/adm_productos_modificar.html', data)


@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    data = {}
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_PRODUCTO', [id, salida])
    salida = salida.getvalue()
    if salida == 1:
        data['mensaje'] = "Producto eliminado"
    else:
        data['mensaje'] = 'El producto no fue eliminado' 
    return redirect(to="adm_productos")


@login_required(login_url='/login/')
@permission_required('app.add_producto')
@permission_required('app.delete_producto')
@permission_required('app.change_producto')
def adm_productos(request):
    listadoProductos = listado_productos()


    data = {
        'productos':listadoProductos,
        'a_p': navbar(),
        'categorias': listado_tipo_productos(),
    }
    if request.method == 'POST' and bool(request.FILES.get('p_imagen', False)) == True:
        p_nombre = request.POST.get('p_nombre')
        p_precio = request.POST.get('p_precio')
        p_stock = request.POST.get('p_stock')
        p_tp = request.POST.get('p_tp')
        p_imagen = request.FILES['p_imagen']
        fs = FileSystemStorage()
        filename = fs.save(p_imagen.name, p_imagen)
        uploaded_file_url = fs.url(filename)
        salida = agregar_producto(p_nombre, p_precio, p_stock, p_tp, uploaded_file_url);
    else:
        p_nombre = request.POST.get('p_nombre')
        p_precio = request.POST.get('p_precio')
        p_stock = request.POST.get('p_stock')
        p_tp = request.POST.get('p_tp')
        p_imagen = None
        salida = agregar_producto(p_nombre, p_precio, p_stock, p_tp, p_imagen);
    if salida == 1:
        data['mensaje'] = "Producto agregado"
    else:
        data['mensaje'] = 'El producto no fue agregado' 
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

@login_required(login_url='/login/')
@permission_required('app.add_empleado')
@permission_required('app.delete_empleado')
@permission_required('app.change_empleado')
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
            user = User.objects.create_user(t_c, t_c, t_p)
            user.first_name = t_pn
            user.last_name = t_pa
            user.save() 
            id_temp = int(t_temp)
            if id_temp == 10:
                user.groups.add(group_vendedor)
            elif id_temp == 30:
                user.groups.add(group_adm)
            elif id_temp == 40:
                user.groups.add(group_tecnico)
            data['mensaje'] = 'Trabajador agregado'
        else:   
            data['mensaje'] = 'El trabajador no fue agregado'
        data['trabajadores'] = listado_trabajadores() 
    return render(request, 'administradores/adm_trabajadores.html', data)   

@permission_required('app.change_empleado')
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
            data['mensaje'] = 'El trabajador no fue modificado' 
        return redirect(to="adm_trabajadores")
    return render(request, 'administradores/adm_trabajadores_modificar.html', data)   

@permission_required('app.delete_empleado')
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

def modificar_cliente(id, c_pn, c_sn, c_pa, c_sa, c_c, c_p, c_d, c_te):
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_CLIENTE', [id, c_pn, c_sn, c_pa, c_sa, c_c, c_p, c_d, c_te, salida])
    return salida.getvalue()

@login_required(login_url='/login/')
@permission_required('app.add_cliente')
@permission_required('app.delete_cliente')
@permission_required('app.change_cliente')
def adm_clientes(request):
    data = {
        'clientes':listado_clientes(),
        'a_c': navbar()
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
            user = User.objects.create_user(c_c, c_c, c_p)
            user.first_name = c_pn
            user.last_name = c_pa
            user.save()
            group = Group.objects.get(name='cliente')
            user.groups.add(group)
            new_user = authenticate(username=c_c,
                                    password=c_p,
                                    )
            if new_user is not None and new_user.is_active:
                login_aut(request,new_user)
                return render(request, 'app/inicio.html')
        else:   
            data['mensaje'] = 'El cliente no fue agregado'
        data['clientes'] = listado_clientes() 
    return render(request, 'administradores/adm_clientes.html', data)   

@permission_required('app.change_cliente')
def adm_modificar_clientes(request, id):
    data = {
        'a_c': navbar(),
        'cliente': listar_cliente(id)
    }
    if request.method == 'POST':
        cm_pn = request.POST.get('cm_pn')
        cm_sn = request.POST.get('cm_sn')
        cm_pa = request.POST.get('cm_pa')
        cm_sa = request.POST.get('cm_sa')
        cm_c = request.POST.get('cm_c')
        cm_p = request.POST.get('cm_p')
        cm_d = request.POST.get('cm_d')
        cm_te = request.POST.get('cm_te')
        salida = modificar_cliente(id, cm_pn, cm_sn, cm_pa, cm_sa, cm_c, cm_p, cm_d, cm_te); 
        if salida == 1:
            data['mensaje'] = "Cliente modificado"
        else:
            data['mensaje'] = 'El cliente no fue modificado' 
        return redirect(to="adm_clientes")
    return render(request, 'administradores/adm_clientes_modificar.html', data)   

@permission_required('app.delete_cliente')
def eliminar_cliente(request, id):
    cursor.callproc('ELIMINAR_CLIENTE', [id])
    return redirect(to="adm_clientes")


### FIN CRUD CLIENTES ###

### CRUD RESEÑAS ###

def agregar_resena(r_u, r_c, r_v, id):
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('INSERTAR_RESENA', [r_u, r_c, r_v, id, salida])
    return salida.getvalue()

def listar_resenas(id):
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("OBTENER_RESENAS", [id, out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista

def resenas(request, id):
    data = {
        'producto': listar_producto(id),
        'prod': navbar(),
        'resena': listar_resenas(id)
    }
    if request.method == 'POST':
        r_u = request.POST.get('r_u')
        r_c = request.POST.get('r_c')
        r_v = request.POST.get('rating')
        salida = agregar_resena(r_u, r_c, r_v, id);
        if salida == 1:
            data['mensaje'] = 'Reseña agregada'
        else:   
            data['mensaje'] = 'La reseña no fue agregada'
        data['resena'] = listar_resenas(id)     
    return render(request, 'app/resenas.html', data)

@login_required(login_url='/login/')
@permission_required('app.delete_resena')
@permission_required('app.change_resena')
def adm_resenas_1(request):
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
        'a_r': navbar()
    }

    return render(request, 'administradores/adm_resenas_1.html', data) 

@permission_required('app.delete_resena')
@permission_required('app.change_resena')
def adm_resenas_2(request, id):
    data = {
        'producto': listar_producto(id),
        'a_r': navbar(),
        'resena': listar_resenas(id)
    }
    if request.method == 'POST':
        r_u = request.POST.get('r_u')
        r_c = request.POST.get('r_c')
        r_v = request.POST.get('rating')
        salida = agregar_resena(r_u, r_c, r_v, id);
        if salida == 1:
            data['mensaje'] = 'Reseña agregada'
        else:   
            data['mensaje'] = 'La reseña no fue agregada'
        data['resena'] = listar_resenas(id)     
    return render(request, 'administradores/adm_resenas_2.html', data)

@permission_required('app.delete_resena')
def eliminar_resena(request, id):
    data = {}
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_RESENA', [id, salida])
    salida = salida.getvalue()
    if salida == 1:
        data['mensaje'] = "Reseña eliminada"
    else:
        data['mensaje'] = 'La reseña no fue eliminada' 
    return redirect(request.META['HTTP_REFERER'])

@permission_required('app.change_resena')
def modificar_resena(id, rm_c, rm_v):
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ACTUALIZAR_RESENA', [id, rm_c, rm_v, salida])
    return salida.getvalue()

def listar_resena(id):
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("OBTENER_RESENA", [id, out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista

@permission_required('app.change_resena')
def adm_modificar_resena(request, id):
    data = {
        'a_r': navbar(),
        'resena': listar_resena(id)
    }
    if request.method == 'POST':
        rm_c = request.POST.get('rm_c')
        rm_v = request.POST.get('rm_v')
        salida = modificar_resena(id, rm_c, rm_v);
        if salida == 1:
            data['mensaje'] = "Reseña modificada"
        else:
            data['mensaje'] = 'La reseña no fue modificada'
        data['resena'] = listar_resena(id) 
    return render(request, 'administradores/adm_resenas_modificar.html', data)
### FIN CRUD RESEÑAS ###
