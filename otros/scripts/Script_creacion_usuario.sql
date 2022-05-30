alter session set "_ORACLE_SCRIPT"=true;

-- USER SQL
CREATE USER innova IDENTIFIED BY "duoc2022"  ;

-- QUOTAS

-- ROLES
GRANT "DBA" TO innova ;
GRANT "CONNECT" TO innova ;
GRANT "RESOURCE" TO innova ;