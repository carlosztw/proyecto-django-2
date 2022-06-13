from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', productos, name='productos'),
    path('servicios/', servicios, name='servicios'),
    path('adm-clientes/', adm_clientes, name='adm_clientes'),
    path('adm-productos/', adm_productos, name='adm_productos'),
    path('adm-productos/modificar/<id>/', adm_modificar_producto, name="modificar_producto"),
    path('eliminarproducto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('adm-servicios/', adm_servicios, name='adm_servicios'),
    path('adm-trabajadores/', adm_trabajadores, name='adm_trabajadores'),
    path('adm-trabajadores/modificar/<id>/', adm_modificar_trabajadores, name='modificar_trabajadores'),
    path('eliminartrabajador/<id>/', eliminar_trabajador, name="eliminar_trabajador"),
    path('registroC/', registroC, name="registroC"),
    path('login/', login, name="login"),


]