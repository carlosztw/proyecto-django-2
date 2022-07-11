------------CRUD SERVICIO----------

--LISTAR TIPO DE Servicio
CREATE OR REPLACE PROCEDURE LISTAR_TIPO_SERVICIO(t_s out SYS_REFCURSOR)
IS

BEGIN
  OPEN t_s FOR SELECT * FROM tipo_servicio ORDER BY id_tipo_servicio;
END LISTAR_TIPO_servicio;

/

------ INSERTAR SERVICIO ----------
CREATE OR REPLACE PROCEDURE INSERTAR_SERVICIO(s_nombre VARCHAR2,
                                              s_correo VARCHAR2,
                                              s_comentario VARCHAR2,
                                              s_imagen VARCHAR2,
                                              s_id_tp_ser NUMBER,
                                              v_salida OUT NUMBER)
IS

BEGIN
    INSERT INTO servicio (id_servicio,nombre_p_ser,correo_ser,comentario_se,fecha_ser,img_ser,id_tipo_servicio) VALUES(seq_servicio.nextval,
                                s_nombre,
                                s_correo,
                                s_comentario,
                                (SELECT TO_CHAR(SYSDATE - 4/24, 'MM-DD-YYYY HH24:MI:SS')
                                FROM DUAL),
                                s_imagen,
                                s_id_tp_ser);
    COMMIT;   
    v_salida := 1;
    EXCEPTION
    WHEN OTHERS THEN
      v_salida := 0;
END INSERTAR_SERVICIO;

/

---------RESCATAR LOS SERVICIOS----------
CREATE OR REPLACE PROCEDURE obtener_servicios(s_cursor OUT SYS_REFCURSOR)
AS
    v_sql VARCHAR2(1000) := 'SELECT s.*, tps.descripcion_ser, ROW_NUMBER() OVER(ORDER BY id_servicio) AS numero_fila
                            FROM servicio s
                            INNER JOIN tipo_servicio tps
                              ON tps.id_tipo_servicio = s.id_tipo_servicio
                            ORDER BY id_servicio';
BEGIN
    OPEN s_cursor FOR v_sql;
END obtener_servicios;

/

--------ELIMINAR SERVICIO----------
CREATE OR REPLACE PROCEDURE ELIMINAR_SERVICIO(s_id_servicio IN NUMBER,
                                             v_salida OUT NUMBER)
AS
    
BEGIN
    DELETE FROM servicio
    WHERE id_servicio = s_id_servicio;
    COMMIT;
    v_salida := 1;
    EXCEPTION
    WHEN OTHERS THEN
      v_salida := 0;
END ELIMINAR_SERVICIO;

/

-----BUSCAR UN SOLO SERVICIO----------
CREATE OR REPLACE PROCEDURE obtener_servicio(s_id_servicio IN NUMBER,
                                             s_cursor OUT SYS_REFCURSOR)
AS
    v_sql VARCHAR2(1000) := 'SELECT s.*, tps.descripcion_ser
                            FROM servicio s
                            INNER JOIN tipo_servicio tps
                              ON tps.id_tipo_servicio = s.id_tipo_servicio
                            WHERE id_servicio = ' || s_id_servicio;
BEGIN
    OPEN s_cursor FOR v_sql;
END obtener_servicio;


/

---------MODIFICAR SERVICIO---------

CREATE OR REPLACE PROCEDURE actualizar_servicio(s_id_ser NUMBER,
                                                s_nombre VARCHAR2,
                                                s_correo VARCHAR2,
                                                s_comentario VARCHAR2,
                                                s_fecha DATE,
                                                s_imagen VARCHAR2,
                                                s_id_tp_ser NUMBER,
                                                v_salida OUT NUMBER)
    AS

BEGIN
    UPDATE servicio
    SET nombre_p_ser = s_nombre,
        correo_ser = s_correo,
        comentario_se = s_comentario,
        fecha_ser = s_fecha,
        img_ser = s_imagen,
        id_tipo_servicio = s_id_tp_ser
    WHERE id_servicio = s_id_ser;
    v_salida := 1;
    EXCEPTION
    WHEN OTHERS THEN
      v_salida := 0;
END actualizar_servicio;

/