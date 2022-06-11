from django.contrib import admin
from .models import Empleado, Producto, Cliente, Servicio, Banco, TipoProducto, TipoServicio, TipoEmpleado

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock', 'id_tipo_producto' ]
    search_fields = ['nombre']
    list_filter = ['id_tipo_producto']
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['rut_emp', 'dv_emp', 'primer_nombre_emp', 'segundo_nombre_emp', 'primer_apellido_emp', 'segundo_apellido_emp', 'correo_emp', 'telefono_emp' ]
    search_fields = ['rut_emp', 'dv_emp', 'primer_nombre_emp', 'segundo_nombre_emp', 'primer_apellido_emp', 'segundo_apellido_emp', 'correo_emp', 'telefono_emp' ]    
    list_filter = ['id_tipo_empleado']
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut_clie', 'dv_clie','primer_nombre_clie', 'segundo_nombre_clie', 'apellido_paterno_clie', 'apellido_materno_clie', 'correo_clie', 'telefono_clie' ]
    search_fields = ['rut_clie', 'dv_clie','primer_nombre_clie', 'segundo_nombre_clie', 'apellido_paterno_clie', 'apellido_materno_clie', 'correo_clie', 'telefono_clie' ]      
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre_p_ser', 'correo_ser', 'comentario_se', 'fecha_ser', 'img_ser', 'id_tipo_servicio' ]
    search_fields = ['nombre_p_ser', 'correo_ser', 'comentario_se', 'fecha_ser', 'img_ser', 'id_tipo_servicio' ]
    list_filter = ['id_tipo_servicio']

    
    
    
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Banco)
admin.site.register(TipoProducto)
admin.site.register(TipoServicio)
admin.site.register(TipoEmpleado)