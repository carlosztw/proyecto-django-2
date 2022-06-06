-- Generado por Oracle SQL Developer Data Modeler 19.4.0.350.1424
--   en:        2022-05-09 20:24:06 CLT
--   sitio:      Oracle Database 11g
--   tipo:      Oracle Database 11g



CREATE TABLE banco (
    id_banco      INTEGER NOT NULL,
    nombre_banco  VARCHAR2(30) NOT NULL
);

ALTER TABLE banco ADD CONSTRAINT banco_pk PRIMARY KEY ( id_banco );

CREATE TABLE cliente (
    rut_clie               INTEGER NOT NULL,
    dv_clie                VARCHAR2(1) NOT NULL,
    primer_nombre_clie     VARCHAR2(50) NOT NULL,
    segundo_nombre_clie    VARCHAR2(50),
    apellido_paterno_clie  VARCHAR2(50) NOT NULL,
    apellido_materno_clie  VARCHAR2(50) NOT NULL,
    correo_clie            VARCHAR2(100) NOT NULL,
    contrasena_clie        VARCHAR2(20) NOT NULL,
    direccion_clie         VARCHAR2(150),
    telefono_clie          INTEGER
);

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( rut_clie );

CREATE TABLE empleado (
    rut_emp               INTEGER NOT NULL,
    dv_emp                VARCHAR2(1) NOT NULL,
    primer_nombre_emp     VARCHAR2(50) NOT NULL,
    segundo_nombre_emp    VARCHAR2(50),
    primer_apellido_emp   VARCHAR2(50) NOT NULL,
    segundo_apellido_emp  VARCHAR2(50) NOT NULL,
    correo_emp            VARCHAR2(150) NOT NULL,
    contrasena_emp        VARCHAR2(20) NOT NULL,
    direccion_emp         VARCHAR2(200) NOT NULL,
    telefono_emp          INTEGER NOT NULL,
    sueldo                INTEGER NOT NULL,
    nro_cuenta            NUMBER(20) NOT NULL,
    id_tipo_empleado      INTEGER NOT NULL,
    id_banco              INTEGER NOT NULL,
    id_tipo_cuenta        INTEGER NOT NULL
);

ALTER TABLE empleado ADD CONSTRAINT empleado_pk PRIMARY KEY ( rut_emp );

CREATE TABLE orden_compra (
    id_orden        INTEGER NOT NULL,
    direccion       VARCHAR2(200) NOT NULL,
    fecha_oc        DATE NOT NULL,
    rut_clie        INTEGER NOT NULL,
    rut_emp         INTEGER NOT NULL,
    id_despacho     INTEGER NOT NULL,
    id_tipo_pago    INTEGER NOT NULL,
    total_final     NUMBER(10) NOT NULL,
    fecha_despacho  DATE NOT NULL,
    firma           CHAR(1) NOT NULL
);

CREATE UNIQUE INDEX orden_compra__idx ON
    orden_compra (
        id_despacho
    ASC );

ALTER TABLE orden_compra ADD CONSTRAINT orden_compra_pk PRIMARY KEY ( id_orden );

CREATE TABLE orden_compra_producto (
    id_producto    INTEGER NOT NULL,
    id_orden       INTEGER NOT NULL,
    total_detalle  NUMBER(10) NOT NULL,
    cantidad_prod  NUMBER(3) NOT NULL
);

ALTER TABLE orden_compra_producto ADD CONSTRAINT or_comp_prod_pk PRIMARY KEY ( id_orden,
                                                                               id_producto );

CREATE TABLE producto (
    id_producto       INTEGER NOT NULL,
    nombre            VARCHAR2(100) NOT NULL,
    precio            INTEGER NOT NULL,
    stock             INTEGER NOT NULL,
    id_tipo_producto  INTEGER NOT NULL,
	imagen            VARCHAR2(300)
);

ALTER TABLE producto ADD CONSTRAINT producto_pk PRIMARY KEY ( id_producto );

CREATE TABLE resena (
    id_resena    INTEGER NOT NULL,
    resena       VARCHAR2(250) NOT NULL,
    id_producto  INTEGER NOT NULL
);

ALTER TABLE resena ADD CONSTRAINT resena_pk PRIMARY KEY ( id_resena );

CREATE TABLE servicio (
    id_servicio       INTEGER NOT NULL,
    nombre_p_ser      VARCHAR2 (60) NOT NULL,
    correo_ser        VARCHAR2(500) NOT NULL,
    comentario_se     VARCHAR2 (1000) NOT NULL,
    fecha_ser         DATE NOT NULL,
    img_ser           VARCHAR2(500),
    id_tipo_servicio  INTEGER NOT NULL
);

ALTER TABLE servicio ADD CONSTRAINT servicio_pk PRIMARY KEY ( id_servicio );


CREATE TABLE servicio_detalle (
    id_orden     INTEGER NOT NULL,
    id_servicio  INTEGER NOT NULL
);

ALTER TABLE servicio_detalle ADD CONSTRAINT ser_det_pk PRIMARY KEY ( id_orden,
                                                                     id_servicio );

CREATE TABLE tipo_cuenta (
    id_tipo_cuenta  INTEGER NOT NULL,
    tipo_cuenta     VARCHAR2(60) NOT NULL
);

ALTER TABLE tipo_cuenta ADD CONSTRAINT tipo_cuenta_pk PRIMARY KEY ( id_tipo_cuenta );

CREATE TABLE tipo_empleado (
    id_tipo_empleado  INTEGER NOT NULL,
    descripcion       VARCHAR2(60) NOT NULL
);

ALTER TABLE tipo_empleado ADD CONSTRAINT tipo_empleado_pk PRIMARY KEY ( id_tipo_empleado );

CREATE TABLE tipo_pago (
    id_tipo_pago  INTEGER NOT NULL,
    tipo_pago     VARCHAR2(60) NOT NULL
);

ALTER TABLE tipo_pago ADD CONSTRAINT tipo_pago_pk PRIMARY KEY ( id_tipo_pago );

CREATE TABLE tipo_producto (
    id_tipo_prod      INTEGER NOT NULL,
    descripcion_prod  VARCHAR2(60) NOT NULL
);

ALTER TABLE tipo_producto ADD CONSTRAINT tipo_producto_pk PRIMARY KEY ( id_tipo_prod );

CREATE TABLE tipo_servicio (
    id_tipo_servicio  INTEGER NOT NULL,
    descripcion_ser   VARCHAR2(60) NOT NULL
);

ALTER TABLE tipo_servicio ADD CONSTRAINT tipo_servicio_pk PRIMARY KEY ( id_tipo_servicio );

ALTER TABLE empleado
    ADD CONSTRAINT emp_banco_fk FOREIGN KEY ( id_banco )
        REFERENCES banco ( id_banco );

ALTER TABLE empleado
    ADD CONSTRAINT emp_tipo_cuenta_fk FOREIGN KEY ( id_tipo_cuenta )
        REFERENCES tipo_cuenta ( id_tipo_cuenta );

ALTER TABLE orden_compra
    ADD CONSTRAINT or_com_clie_fk FOREIGN KEY ( rut_clie )
        REFERENCES cliente ( rut_clie );

ALTER TABLE orden_compra
    ADD CONSTRAINT or_com_emp_fk FOREIGN KEY ( rut_emp )
        REFERENCES empleado ( rut_emp );

ALTER TABLE orden_compra_producto
    ADD CONSTRAINT or_com_prod_fk FOREIGN KEY ( id_orden )
        REFERENCES orden_compra ( id_orden );

ALTER TABLE orden_compra_producto
    ADD CONSTRAINT or_com_prod_fkv2 FOREIGN KEY ( id_producto )
        REFERENCES producto ( id_producto );

ALTER TABLE orden_compra
    ADD CONSTRAINT or_com_tip_pag_fk FOREIGN KEY ( id_tipo_pago )
        REFERENCES tipo_pago ( id_tipo_pago );

ALTER TABLE resena
    ADD CONSTRAINT res_prod_fk FOREIGN KEY ( id_producto )
        REFERENCES producto ( id_producto );

ALTER TABLE servicio_detalle
    ADD CONSTRAINT ser_det_or_com_fk FOREIGN KEY ( id_orden )
        REFERENCES orden_compra ( id_orden );

ALTER TABLE servicio_detalle
    ADD CONSTRAINT ser_det_ser_fk FOREIGN KEY ( id_servicio )
        REFERENCES servicio ( id_servicio );

ALTER TABLE producto
    ADD CONSTRAINT tip_prod_fk FOREIGN KEY ( id_tipo_producto )
        REFERENCES tipo_producto ( id_tipo_prod );

ALTER TABLE empleado
    ADD CONSTRAINT tipo_empleado_fk FOREIGN KEY ( id_tipo_empleado )
        REFERENCES tipo_empleado ( id_tipo_empleado );

ALTER TABLE servicio
    ADD CONSTRAINT tipo_ser_fk FOREIGN KEY ( id_tipo_servicio )
        REFERENCES tipo_servicio ( id_tipo_servicio );



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            14
-- CREATE INDEX                             1
-- ALTER TABLE                             27
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
