DROP SEQUENCE seq_banco;
CREATE SEQUENCE seq_banco START WITH 10 INCREMENT BY 10;

INSERT INTO banco VALUES(SEQ_BANCO.nextval, 'Banco Estado');
INSERT INTO banco VALUES(SEQ_BANCO.nextval, 'Banco de Chile');
INSERT INTO banco VALUES(SEQ_BANCO.nextval, 'Santander');
INSERT INTO banco VALUES(SEQ_BANCO.nextval, 'Scotiabank');
INSERT INTO banco VALUES(SEQ_BANCO.nextval, 'Banco Itau');
---------------------------------------------------------------
DROP SEQUENCE seq_tp_prod;
CREATE SEQUENCE seq_tp_prod START WITH 100;

INSERT INTO tipo_producto VALUES (seq_tp_prod.nextval, 'Procesadores' );
INSERT INTO tipo_producto VALUES (seq_tp_prod.nextval, 'Tarjetas de video' );
INSERT INTO tipo_producto VALUES (seq_tp_prod.nextval, 'RAM' );
INSERT INTO tipo_producto VALUES (seq_tp_prod.nextval, 'Discos Duros' );
INSERT INTO tipo_producto VALUES (seq_tp_prod.nextval, 'Placas Madres' );

---------------------------------------------------------------
DROP SEQUENCE seq_prod;
CREATE SEQUENCE seq_prod START WITH 5 INCREMENT BY 5;

INSERT INTO producto VALUES(SEQ_PROD.nextval, 'AMD CPU AMD sAM4', 40000, 17, 100, null);

---------------------------------------------------------------
DROP SEQUENCE seq_tp_ser;
CREATE SEQUENCE seq_tp_ser START WITH 5 INCREMENT BY 5;

INSERT INTO tipo_servicio VALUES (SEQ_TP_SER.nextval, 'Reparaciones' );
INSERT INTO tipo_servicio VALUES (SEQ_TP_SER.nextval, 'Armados' );
INSERT INTO tipo_servicio VALUES (SEQ_TP_SER.nextval, 'Cotizaciones' );

---------------------------------------------------------------
DROP SEQUENCE seq_tp_emp;
CREATE SEQUENCE seq_tp_emp START WITH 10 INCREMENT BY 10;

INSERT INTO tipo_empleado VALUES (SEQ_TP_EMP.nextval, 'Vendedor' ) ;
INSERT INTO tipo_empleado VALUES (SEQ_TP_EMP.nextval, 'Despachador' ) ;
INSERT INTO tipo_empleado VALUES (SEQ_TP_EMP.nextval, 'Administrador' ) ;
INSERT INTO tipo_empleado VALUES (SEQ_TP_EMP.nextval, 'RRHH' ) ;

---------------------------------------------------------------
DROP SEQUENCE seq_pago;
CREATE SEQUENCE seq_pago START WITH 50 INCREMENT BY 50;

INSERT INTO tipo_pago VALUES (SEQ_PAGO.nextval, 'Debito');
INSERT INTO tipo_pago VALUES (SEQ_PAGO.nextval, 'Credito');

---------------------------------------------------------------
DROP SEQUENCE seq_tp_cnta;
CREATE SEQUENCE seq_tp_cnta START WITH 50 INCREMENT BY 50;

INSERT INTO tipo_cuenta VALUES (SEQ_TP_CNTA.nextval, 'Cuenta corriente') ;
INSERT INTO tipo_cuenta VALUES (SEQ_TP_CNTA.nextval, 'Cuenta rut') ;
INSERT INTO tipo_cuenta VALUES (SEQ_TP_CNTA.nextval, 'Cuenta vista') ;

---------------------------------------------------------------

INSERT INTO empleado VALUES ( 19742774, 7, 'Mila', 'Alejandra', 'Darat', 'Morales', 'midaratm@innoca.cl', 'innova123', 'Puente alto', 943220976, 420000, 0001134567288, 40, 20, 150);

---------------------------------------------------------------

INSERT INTO cliente VALUES (8117450, 4, 'Rosario', ' ', 'Soto', ' ', 'rsoto@gmail.com', 'cliente123', 'Puente alto', 943526784);

---------------------------------------------------------------

DROP SEQUENCE seq_resn;
CREATE SEQUENCE seq_resn START WITH 1;

DROP SEQUENCE seq_servicio;
CREATE SEQUENCE seq_servicio START WITH 10 INCREMENT BY 10;
INSERT INTO servicio VALUES(SEQ_SERVICIO.nextval,'Ernesto Arredondo','ern.arredondo@gmail.com','mi computador normalmente envia un fondo azul en donde se cae el sistema','01/06/2022','https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Bsodwindows10.png/640px-Bsodwindows10.png',5);


---------------------------------------------------------------


---------------------------------------------------------------