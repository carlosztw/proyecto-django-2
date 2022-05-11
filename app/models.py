# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Banco(models.Model):
    id_banco = models.AutoField(primary_key=True)
    nombre_banco = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'banco'
    def __str__(self):
        return self.nombre_banco

class Cliente(models.Model):
    rut_clie = models.BigIntegerField(primary_key=True)
    dv_clie = models.CharField(max_length=1)
    primer_nombre_clie = models.CharField(max_length=50)
    segundo_nombre_clie = models.CharField(max_length=50, blank=True, null=True)
    apellido_paterno_clie = models.CharField(max_length=50)
    apellido_materno_clie = models.CharField(max_length=50)
    correo_clie = models.CharField(max_length=100)
    contrasena_clie = models.CharField(max_length=20)
    direccion_clie = models.CharField(max_length=150, blank=True, null=True)
    telefono_clie = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'
    def __str__(self):
        return str(self.rut_clie)

class Empleado(models.Model):
    rut_emp = models.BigIntegerField(primary_key=True)
    dv_emp = models.CharField(max_length=1)
    primer_nombre_emp = models.CharField(max_length=50)
    segundo_nombre_emp = models.CharField(max_length=50, blank=True, null=True)
    primer_apellido_emp = models.CharField(max_length=50)
    segundo_apellido_emp = models.CharField(max_length=50)
    correo_emp = models.CharField(max_length=150)
    contrasena_emp = models.CharField(max_length=20)
    direccion_emp = models.CharField(max_length=200)
    telefono_emp = models.BigIntegerField()
    sueldo = models.BigIntegerField()
    nro_cuenta = models.BigIntegerField()
    id_tipo_empleado = models.ForeignKey('TipoEmpleado', models.DO_NOTHING, db_column='id_tipo_empleado')
    id_banco = models.ForeignKey(Banco, models.DO_NOTHING, db_column='id_banco')
    id_tipo_cuenta = models.ForeignKey('TipoCuenta', models.DO_NOTHING, db_column='id_tipo_cuenta')

    class Meta:
        managed = False
        db_table = 'empleado'
    def __str__(self):
        return str(self.rut_emp)

class OrdenCompra(models.Model):
    id_orden = models.BigIntegerField(primary_key=True)
    direccion = models.CharField(max_length=200)
    fecha_oc = models.DateField()
    rut_clie = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='rut_clie')
    rut_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='rut_emp')
    id_despacho = models.BigIntegerField(unique=True)
    id_tipo_pago = models.ForeignKey('TipoPago', models.DO_NOTHING, db_column='id_tipo_pago')
    total_final = models.IntegerField()
    fecha_despacho = models.DateField()
    firma = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'orden_compra'
    def __str__(self):
        return self.id_orden

class OrdenCompraProducto(models.Model):
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    id_orden = models.OneToOneField(OrdenCompra, models.DO_NOTHING, db_column='id_orden', primary_key=True)
    total_detalle = models.IntegerField()
    cantidad_prod = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orden_compra_producto'
        unique_together = (('id_orden', 'id_producto'),)
    def __str__(self):
        return self.id_producto

class Producto(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.BigIntegerField()
    imagen = models.BinaryField(blank=True, null=True)
    stock = models.BigIntegerField()
    id_tipo_producto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='id_tipo_producto')

    class Meta:
        managed = False
        db_table = 'producto'
    def __str__(self):
        return self.nombre

class Resena(models.Model):
    id_resena = models.BigIntegerField(primary_key=True)
    resena = models.CharField(max_length=250)
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'resena'
    def __str__(self):
        return self.id_resena

class Servicio(models.Model):
    id_servicio = models.BigIntegerField(primary_key=True)
    fecha_ser = models.DateField()
    adjunto_ser = models.BinaryField(blank=True, null=True)
    comentario = models.CharField(max_length=500)
    id_tipo_servicio = models.ForeignKey('TipoServicio', models.DO_NOTHING, db_column='id_tipo_servicio')

    class Meta:
        managed = False
        db_table = 'servicio'
    def __str__(self):
        return self.id_servicio

class ServicioDetalle(models.Model):
    id_orden = models.OneToOneField(OrdenCompra, models.DO_NOTHING, db_column='id_orden', primary_key=True)
    id_servicio = models.ForeignKey(Servicio, models.DO_NOTHING, db_column='id_servicio')

    class Meta:
        managed = False
        db_table = 'servicio_detalle'
        unique_together = (('id_orden', 'id_servicio'),)
    def __str__(self):
        return self.id_servicio

class TipoCuenta(models.Model):
    id_tipo_cuenta = models.BigIntegerField(primary_key=True)
    tipo_cuenta = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'
    def __str__(self):
        return self.tipo_cuenta

class TipoEmpleado(models.Model):
    id_tipo_empleado = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_empleado'
    def __str__(self):
        return self.descripcion

class TipoPago(models.Model):
    id_tipo_pago = models.BigIntegerField(primary_key=True)
    tipo_pago = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_pago'
    def __str__(self):
        return self.tipo_pago

class TipoProducto(models.Model):
    id_tipo_prod = models.BigIntegerField(primary_key=True)
    descripcion_prod = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_producto'
    def __str__(self):
        return self.descripcion_prod

class TipoServicio(models.Model):
    id_tipo_servicio = models.BigIntegerField(primary_key=True)
    descripcion_ser = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_servicio'
    def __str__(self):
        return self.descripcion_ser