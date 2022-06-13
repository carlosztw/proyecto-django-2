from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', productos, name='productos'),
    path('resenas/<id>/', resenas, name='resenas'),
    path('servicios/', servicios, name='servicios'),
    path('adm-clientes/', adm_clientes, name='adm_clientes'),
    path('adm-clientes/modificar/<id>/', adm_modificar_clientes, name='modificar_cliente'),
    path('eliminarcliente/<id>/', eliminar_cliente, name="eliminar_cliente"),
    path('adm-productos/', adm_productos, name='adm_productos'),
    path('adm-productos/modificar/<id>/', adm_modificar_producto, name="modificar_producto"),
    path('eliminarproducto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('adm-servicios/', adm_servicios, name='adm_servicios'),
    path('adm-trabajadores/', adm_trabajadores, name='adm_trabajadores'),
    path('adm-trabajadores/modificar/<id>/', adm_modificar_trabajadores, name='modificar_trabajadores'),
    path('eliminartrabajador/<id>/', eliminar_trabajador, name="eliminar_trabajador"),
<<<<<<< HEAD
    path('registroC/', registroC, name="registroC"),
    path('login/', login, name="LOG"),
    path('cerrar/', cerrar_sesion, name="CERRAR"),


=======
    path('adm-resenas-1/', adm_resenas_1, name="adm_resenas_1"),
    path('adm-resenas-2/<id>/', adm_resenas_2, name="adm_resenas_2"),
    path('eliminarresena/<id>/', eliminar_resena, name="eliminar_resena"),
    path('modificarresena/<id>/', adm_modificar_resena, name="modificar_resena"),
>>>>>>> 2ca1bec6abd073b35bf2987383296a56a2bf3d64
]