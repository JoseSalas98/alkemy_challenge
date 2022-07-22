CREATE TABLE IF NOT EXISTS "cultural_info" (
  "created_date"          DATE DEFAULT CURRENT_DATE,
  "cod_localidad"				  INTEGER,
  "id_provincia" 		      INTEGER,
  "id_departamento"				INTEGER, 
  "categoria"			        VARCHAR(200), 
  "provincia"			        VARCHAR(200),
  "localidad"			        VARCHAR(200),
  "nombre"			          VARCHAR(200),
  "domicilio"				      VARCHAR(200),
  "codigo_postal"			    VARCHAR(200),
  "numero_de_telefono"    VARCHAR(200),
  "mail"                  VARCHAR(200),
  "web"                   VARCHAR(200)
);
