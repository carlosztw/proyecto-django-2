from django.shortcuts import render, redirect
from django.db import connection
from django.core.paginator import Page, Paginator
from django.http import Http404
from django.core.files.storage import FileSystemStorage
from .views import *
from carro import views
import cx_Oracle
#importar el modelo de la tabla user
from django.contrib.auth.models import User
#importar libreria para autentificar usuarios 
from django.contrib.auth import authenticate,logout,login as login_aut
#importar libreria decoradora que evita el ingreso a las paginas 
from django.contrib.auth.decorators import login_required
from transbank.webpay.webpay_plus.transaction import *
from transbank.webpay.webpay_plus.transaction import Transaction
import random
from flask import render_template, request
# Create your views here.
django_cursor = connection.cursor()
cursor = django_cursor.connection.cursor()


### Transbank ###

def webpay_plus_create():
    print("Webpay Plus Transaction.create")
    buy_order = str(random.randrange(1000000, 99999999))
    session_id = str(random.randrange(1000000, 99999999))
    amount = random.randrange(10000, 1000000)
    return_url = request.url_root + 'webpay-plus/commit'

    create_request = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url
    }

    response = (Transaction()).create(buy_order, session_id, amount, return_url)

    print(response)

    return render_template('webpay/plus/create.html', request=create_request, response=response)

### CRUD SERVICIOS ###
def listado_tipo_servicios():
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("LISTAR_TIPO_SERVICIO", [out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista

def agregar_servicio(s_nombre, s_correo, s_comentario, s_imagen, s_ts):
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('INSERTAR_SERVICIO', [s_nombre, s_correo, s_comentario, s_imagen, s_ts, salida])
    return salida.getvalue()

def servicios(request):
    data={
        'servicios': navbar(),
        'listado_servicios': listado_tipo_servicios()
    }
    if request.method == 'POST':
        s_nombre = request.POST.get('s_nombre')
        s_correo = request.POST.get('s_correo')
        s_comentario = request.POST.get('s_comentario')
        s_imagen = request.POST.get('s_imagen')
        s_ts = request.POST.get('s_ts')
        salida = agregar_servicio(s_nombre, s_correo, s_comentario, s_imagen, s_ts)
        if salida == 1:
            data['mensaje'] = "Servicio enviado"
        else:
            data['mensaje'] = 'Error, el servicio no fue enviado' 
    return render(request, 'app/servicios.html', data)

def adm_servicios(request):
    data={
        'a_s': navbar(),
        'servicio': listado_servicios()
    }
    return render(request, 'administradores/adm_servicios.html', data)   

def listado_servicios():
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("OBTENER_SERVICIOS", [out_cur])
    lista = []
    for i in out_cur:
        lista.append(i)
    return lista

def eliminar_servicio(request, id):
    data = {}
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('ELIMINAR_SERVICIO', [id, salida])
    salida = salida.getvalue()
    if salida == 1:
        data['mensaje'] = "Servicio eliminado"
    else:
        data['mensaje'] = 'El servicio no fue eliminado' 
    return redirect(to="adm_servicios")
### FIN CRUD SERVICIOS ###

### LOGIN ###
def cerrar_sesion(request):
    logout(request)
    views.limpiar_carro(request)
    return render(request, 'app/inicio.html')


def login(request):
    contexto = {
        'login': navbar()
    }
    mensaje=""
    if request.POST:
        nombre = request.POST.get("txtUsuario")
        contra = request.POST.get("txtcontrasena")
        us = authenticate(request,username=nombre,password=contra)
        if us is not None and us.is_active:
            login_aut(request,us)
            return render(request, 'app/inicio.html')
        else:
            contexto['mensaje']="Usuario y/o contraseña incorrecta"
          
    return render(request, 'app/login.html', contexto)   

def registroC(request):
    data = {
        'registrar': navbar()
    }
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
    return render(request, 'app/registroC.html', data)
### FIN DEL LOGIN ### 
def carrito(request):

    return render(request, 'app/carro.html')   
### Carrito ###