# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from distutils.command.upload import upload
from django.db import models
from models import set_sql_for_field

class Banco(models.Model):
    id_banco = models.AutoField(primary_key=True)
    nombre_banco = models.CharField(max_length=30)
 
    class Meta:
        managed = False
        db_table = 'banco'
    def __str__(self):
        return self.nombre_banco


    @set_sql_for_field('id_banco', 'select seq_banco.nextval from dual')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



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
    id_orden = models.AutoField(primary_key=True)
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
    @set_sql_for_field('id_orden', 'select seq_orden.nextval from dual')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

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
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.BigIntegerField()
    stock = models.BigIntegerField()
    id_tipo_producto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='id_tipo_producto')
    imagen = models.ImageField(upload_to="", null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'producto'
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
        
    @set_sql_for_field('id_producto', 'select seq_prod.nextval from dual')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Resena(models.Model):
    id_resena = models.AutoField(primary_key=True)
    usuario_resena = models.CharField(max_length=100)
    comentario = models.CharField(max_length=250)
    valoracion = models.IntegerField(default=0)
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'resena'
    def __str__(self):
        return self.id_resena
    @set_sql_for_field('id_resena', 'select seq_resn.nextval from dual')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    fecha_ser = models.DateField()
    adjunto_ser = models.BinaryField(blank=True, null=True)
    comentario = models.CharField(max_length=500)
    id_tipo_servicio = models.ForeignKey('TipoServicio', models.DO_NOTHING, db_column='id_tipo_servicio')

    class Meta:
        managed = False
        db_table = 'servicio'
    def __str__(self):
        return self.id_servicio
    @set_sql_for_field('id_servicio', 'select seq_serv.nextval from dual')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

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
    id_tipo_cuenta = models.AutoField(primary_key=True)
    tipo_cuenta = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'
    def __str__(self):
        return self.tipo_cuenta
    @set_sql_for_field('id_tipo_cuenta', 'select seq_tp_cnta.nextval from dual')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class TipoEmpleado(models.Model):
    id_tipo_empleado = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_empleado'
    def __str__(self):
        return self.descripcion
    @set_sql_for_field('id_tipo_empleado', 'select seq_tp_emp.nextval from dual')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class TipoPago(models.Model):
    id_tipo_pago = models.AutoField(primary_key=True)
    tipo_pago = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_pago'
    def __str__(self):
        return self.tipo_pago
    @set_sql_for_field('id_tipo_pago', 'select seq_pago.nextval from dual')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class TipoProducto(models.Model):
    id_tipo_prod = models.AutoField(primary_key=True)
    descripcion_prod = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_producto'
    def __str__(self):
        return self.descripcion_prod

    @set_sql_for_field('id_tipo_prod', 'select seq_tp_prod.nextval from dual')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class TipoServicio(models.Model):
    id_tipo_servicio = models.AutoField(primary_key=True)
    descripcion_ser = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_servicio'
    def __str__(self):
        return self.descripcion_ser
    
    @set_sql_for_field('id_tipo_servicio', 'select seq_tp_ser.nextval from dual')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

