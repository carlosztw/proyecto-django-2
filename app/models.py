# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Banco(models.Model):
    id_banco = models.AutoField(primary_key=True)
    nombre_banco = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'banco'


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


class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    comentario = models.CharField(max_length=500)
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio')

    class Meta:
        managed = False
        db_table = 'comentario'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    id_tipo_empleado = models.ForeignKey('TipoEmpleado', models.DO_NOTHING, db_column='id_tipo_empleado')
    nro_cuenta = models.BigIntegerField(blank=True, null=True)
    id_banco = models.ForeignKey(Banco, models.DO_NOTHING, db_column='id_banco')
    id_tipo_cuenta = models.ForeignKey('TipoCuenta', models.DO_NOTHING, db_column='id_tipo_cuenta')

    class Meta:
        managed = False
        db_table = 'empleado'


class OrdenCompra(models.Model):
    id_orden = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=200)
    fecha_oc = models.DateField()
    rut_clie = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='rut_clie')
    rut_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='rut_emp')
    id_tipo_pago = models.ForeignKey('TipoPago', models.DO_NOTHING, db_column='id_tipo_pago')
    total_final = models.IntegerField()
    fecha_despacho = models.DateField()
    firma = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_compra'


class OrdenCompraProducto(models.Model):
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    id_orden = models.OneToOneField(OrdenCompra, models.DO_NOTHING, db_column='id_orden', primary_key=True)
    total_detalle = models.IntegerField()
    cantidad_prod = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orden_compra_producto'
        unique_together = (('id_orden', 'id_producto'),)


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.BigIntegerField()
    stock = models.BigIntegerField()
    id_tipo_prod = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='id_tipo_prod')

    class Meta:
        managed = False
        db_table = 'producto'


class Resena(models.Model):
    id_resena = models.AutoField(primary_key=True)
    resena = models.CharField(max_length=250)
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'resena'


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    fecha_ser = models.DateField()
    adjunto_ser = models.BinaryField(blank=True, null=True)
    id_tipo_servicio = models.ForeignKey('TipoServicio', models.DO_NOTHING, db_column='id_tipo_servicio')

    class Meta:
        managed = False
        db_table = 'servicio'


class ServicioDetalle(models.Model):
    id_orden = models.OneToOneField(OrdenCompra, models.DO_NOTHING, db_column='id_orden', primary_key=True)
    id_servicio = models.ForeignKey(Servicio, models.DO_NOTHING, db_column='id_servicio')

    class Meta:
        managed = False
        db_table = 'servicio_detalle'
        unique_together = (('id_orden', 'id_servicio'),)


class TipoCuenta(models.Model):
    id_tipo_cuenta = models.AutoField(primary_key=True)
    tipo_cuenta = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'


class TipoEmpleado(models.Model):
    id_tipo_empleado = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_empleado'


class TipoPago(models.Model):
    id_tipo_pago = models.AutoField(primary_key=True)
    tipo_pago = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_pago'


class TipoProducto(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)
    descripcion_prod = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TipoServicio(models.Model):
    id_tipo_servicio = models.AutoField(primary_key=True)
    descripcion_ser = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_servicio'
