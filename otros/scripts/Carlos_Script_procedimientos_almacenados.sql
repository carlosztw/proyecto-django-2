------------------------CRUD DE PRODUCTOS------------------------
--INSERTAR UN PRODUCTO:
CREATE OR REPLACE PROCEDURE INSERTAR_PRODUCTO(p_nombre VARCHAR2,
                                              p_precio NUMBER,
                                              p_stock NUMBER,
                                              p_id_tipo_prod NUMBER,
                                              p_imagen VARCHAR2,
                                              v_salida OUT NUMBER)
IS
    
BEGIN
    INSERT INTO producto (id_producto, nombre, precio, stock, id_tipo_producto, imagen) VALUES(seq_prod.nextval,
                                p_nombre,
                                p_precio,
                                p_stock,
                                p_id_tipo_prod,
                                p_imagen);
    COMMIT;   
    v_salida := 1;
    EXCEPTION
    WHEN OTHERS THEN
      v_salida := 0;
END INSERTAR_PRODUCTO;

/
--RESCATAR A TODOS LOS PRODUCTOS:

CREATE OR REPLACE PROCEDURE obtener_productos(p_cursor OUT SYS_REFCURSOR)
AS
    v_sql VARCHAR2(1000) := 'SELECT p.*, tp.descripcion_prod
                            FROM producto p
                            INNER JOIN tipo_producto tp
                              ON tp.id_tipo_prod = p.id_tipo_producto
                            ORDER BY id_producto';
BEGIN
    OPEN p_cursor FOR v_sql;
END obtener_productos;

/

--eliminar un producto:

CREATE OR REPLACE PROCEDURE ELIMINAR_PRODUCTO(p_id_producto IN NUMBER)
AS
    
BEGIN
    DELETE FROM producto
    WHERE id_producto = p_id_producto;
    COMMIT;
END ELIMINAR_PRODUCTO;

/

--buscar solamente un producto:
CREATE OR REPLACE PROCEDURE obtener_producto(p_id_producto IN NUMBER,
                                             p_cursor OUT SYS_REFCURSOR)
AS
    v_sql VARCHAR2(1000) := 'SELECT p.*, tp.descripcion_prod
                            FROM producto p
                            INNER JOIN tipo_producto tp
                              ON tp.id_tipo_prod = p.id_tipo_producto
                            WHERE id_producto = ' || p_id_producto;
BEGIN
    OPEN p_cursor FOR v_sql;
END obtener_producto;


/

--Modificar un producto:

CREATE OR REPLACE PROCEDURE actualizar_producto(p_id_pro NUMBER,
                                                p_nombre VARCHAR2,
                                                p_precio NUMBER,
                                                p_stock NUMBER,
                                                p_id_tp_prod NUMBER,
                                                p_imagen VARCHAR2,
                                                v_salida OUT NUMBER)
AS

BEGIN
    UPDATE producto
    SET nombre = p_nombre,
        precio = p_precio,
        stock = p_stock,
        id_tipo_producto = p_id_tp_prod,
        imagen = p_imagen
    WHERE id_producto = p_id_pro;
    v_salida := 1;
    EXCEPTION
    WHEN OTHERS THEN
      v_salida := 0;
END actualizar_producto;

/

--LISTAR TIPO DE PRODUCTO
CREATE OR REPLACE PROCEDURE LISTAR_TIPO_PRODUCTO(t_p out SYS_REFCURSOR)
IS

BEGIN
  OPEN t_p FOR SELECT * FROM tipo_producto ORDER BY id_tipo_prod;
END LISTAR_TIPO_PRODUCTO;

/

------------------------CRUD DE TRABAJADORES------------------------
--LISTAR BANCO
CREATE OR REPLACE PROCEDURE LISTAR_BANCO(t_p out SYS_REFCURSOR)
IS

BEGIN
  OPEN t_p FOR SELECT * FROM banco ORDER BY id_banco;
END LISTAR_BANCO;

/

--LISTAR TIPO CUENTA
CREATE OR REPLACE PROCEDURE LISTAR_TIPO_CUENTA(t_p out SYS_REFCURSOR)
IS

BEGIN
  OPEN t_p FOR SELECT * FROM tipo_cuenta ORDER BY id_tipo_cuenta;
END LISTAR_TIPO_CUENTA;

/

--LISTAR BANCO
CREATE OR REPLACE PROCEDURE LISTAR_TIPO_EMPLEADO(t_p out SYS_REFCURSOR)
IS

BEGIN
  OPEN t_p FOR SELECT * FROM tipo_empleado ORDER BY id_tipo_empleado;
END LISTAR_TIPO_EMPLEADO;

/

--LISTAR TRABAJADORES
CREATE OR REPLACE PROCEDURE obtener_trabajadores(p_cursor OUT SYS_REFCURSOR)
AS
    v_sql VARCHAR2(1500) := 'SELECT e.*, te.descripcion, b.nombre_banco, tc.tipo_cuenta, ROW_NUMBER() OVER(ORDER BY e.rut_emp) AS numero_fila
                            FROM empleado e
                            INNER JOIN tipo_empleado te
                              ON te.id_tipo_empleado = e.id_tipo_empleado
                            INNER JOIN banco b
                              ON b.id_banco = e.id_banco
                            INNER JOIN tipo_cuenta tc
                              ON tc.id_tipo_cuenta = e.id_tipo_cuenta
                            ORDER BY e.rut_emp';
BEGIN
    OPEN p_cursor FOR v_sql;
END obtener_trabajadores;

/

--INSERTAR TRABAJADOR
CREATE OR REPLACE PROCEDURE INSERTAR_TRABAJADOR(t_rut number,
                                                t_dv varchar2,
                                                t_pn varchar2,
                                                t_sn varchar2,
                                                t_pa varchar2,
                                                t_sa varchar2,
                                                t_c varchar2,
                                                t_p varchar2,
                                                t_d varchar2,
                                                t_te number,
                                                t_s number,
                                                t_nc number,
                                                t_temp number,
                                                t_b number,
                                                t_tc number,
                                                v_salida out number)
IS
    
BEGIN
    INSERT INTO empleado(rut_emp, dv_emp, primer_nombre_emp, segundo_nombre_emp, primer_apellido_emp, segundo_apellido_emp,
                         correo_emp, contrasena_emp, direccion_emp, telefono_emp, sueldo, nro_cuenta, id_tipo_empleado,
                         id_banco, id_tipo_cuenta)VALUES(t_rut,
                                t_dv,
                                t_pn,
                                t_sn,
                                t_pa,
                                t_sa,
                                t_c,
                                t_p,
                                t_d,
                                t_te,
                                t_s,
                                t_nc,
                                t_temp,
                                t_b,
                                t_tc);
    COMMIT; 
    v_salida:=1;
  
    EXCEPTION
    WHEN OTHERS THEN
      v_salida := 0;
END INSERTAR_TRABAJADOR;
/

-- ELIMINAR TRABAJADOR

CREATE OR REPLACE PROCEDURE ELIMINAR_TRABAJADOR(t_rut_emp IN NUMBER)
AS
    
BEGIN
    DELETE FROM empleado
    WHERE rut_emp = t_rut_emp;
    COMMIT;
END ELIMINAR_TRABAJADOR;

/

-- LISTAR TRABAJADOR
CREATE OR REPLACE PROCEDURE obtener_trabajador(t_rut_emp IN NUMBER,
                                                 p_cursor OUT SYS_REFCURSOR)
AS
    v_sql VARCHAR2(1500) := 'SELECT e.*, te.descripcion, b.nombre_banco, tc.tipo_cuenta, ROW_NUMBER() OVER(ORDER BY e.rut_emp) AS numero_fila
                            FROM empleado e
                            INNER JOIN tipo_empleado te
                              ON te.id_tipo_empleado = e.id_tipo_empleado
                            INNER JOIN banco b
                              ON b.id_banco = e.id_banco
                            INNER JOIN tipo_cuenta tc
                              ON tc.id_tipo_cuenta = e.id_tipo_cuenta
                            WHERE e.rut_emp = ' || t_rut_emp;
BEGIN
    OPEN p_cursor FOR v_sql;
END obtener_trabajador;

/
-- MODIFICAR TRABAJADOR
CREATE OR REPLACE PROCEDURE MODIFICAR_TRABAJADOR(t_rut number,
                                                t_pn varchar2,
                                                t_sn varchar2,
                                                t_pa varchar2,
                                                t_sa varchar2,
                                                t_c varchar2,
                                                t_p varchar2,
                                                t_d varchar2,
                                                t_te number,
                                                t_s number,
                                                t_nc number,
                                                t_temp number,
                                                t_b number,
                                                t_tc number,
                                                v_salida out number)
IS
    
BEGIN
    UPDATE empleado
    SET primer_nombre_emp = t_pn, 
        segundo_nombre_emp = t_sn, 
        primer_apellido_emp = t_pa, 
        segundo_apellido_emp = t_sa,
        correo_emp = t_c, 
        contrasena_emp = t_p, 
        direccion_emp = t_d, 
        telefono_emp = t_te, 
        sueldo = t_s, 
        nro_cuenta = t_nc, 
        id_tipo_empleado = t_temp,
        id_banco = t_b, 
        id_tipo_cuenta = t_tc
    WHERE rut_emp = t_rut;
    COMMIT; 
    v_salida:=1;
  
    EXCEPTION
    WHEN OTHERS THEN
      v_salida := 0;
END MODIFICAR_TRABAJADOR;

/