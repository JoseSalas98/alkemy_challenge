<head>
    <meta http-equiv="Content-Type"content="text/html"charset="utf-8">
    <title>VIAJES ALEGRES</title>
    <link href="./css_estilos/estilo_01.css"rel="stylesheet"type="text/css"> 
</head>

<div id='id0' > </div>

<body>
    <img src="./css_estilos/JSLogoFondoClaro.png" style="float: right" width="250" height="230">
    <h1> <b> Dockerización de ETL Basado en Web-Scraping </b> </h1>
</body>

<body>
    <h2> <b> Índice </b> </h2>
</body>

1.  [<p style="font-family: rubik"> Enunciado del Reto. </p>](#id1)
2.  [<p style="font-family: rubik"> Propuesta Metodológica. </p>](#id2)
3.  [<p style="font-family: rubik"> Herramientas Utilizadas. </p>](#id3)
4.  [<p style="font-family: rubik"> Análisis Exploratorio de Datos. </p>](#id4)
5.  [<p style="font-family: rubik"> Variables de Entorno. </p>](#id5)
6.  [<p style="font-family: rubik"> Configuración del Motor de Base de Datos (<b>Postgres</b>). </p>](#id6)
7.  [<p style="font-family: rubik"> Configuración de la Conexión con <b> Postgres</b>. </p>](#id7)
8.  [<p style="font-family: rubik"> Configuración de la Interfaz Gráfica para la Base de Datos. (<b> Pgadmin4</b>). </p>](#id8)
9.  [<p style="font-family: rubik"> Ejecución. </p>](#id9)

---

<div id='id1' > </div>

<body>
    <h2> <b> Enunciado del Reto </b> </h2>
    <p>
    Para acceder al enunciado del reto haz clíck en:
    </p>
</body>

[<p style="font-family: rubik"> Enunciado </p>](alkemy_challenge.pdf.pdf)

[<p style="font-family: rubik"> Índice </p> ](#id0)

---

<div id='id2' > </div>

<body>
    <h2> <b> Propuesta Metodológica </b> </h2>
    <p>
    A la hora de hacer el despliegue y ejecución del proceso de extracción, transformación y carga (<b>ETL</b>: Extract, Transform and Load ) es necesario garantizar que este sea capaz de ejecutarse en cualquier ordenador, es por ello que se debe definir un entorno de desarrollo, el cual pueda ser ejecutado por el usuario para que el ETL corra sobre este y no localmente, de tal forma que la ejecución no sea interrumpida por errores asociados a dependencias o versionado. <br>
    <br>
    Para el desarrollo y ejecución se implemento Docker y a partir de este se levantaron tres contenedores, en cada uno de los cuales corre uno de tres servicios, respectivamente: <b> Postgres </b>, <b> Pgadmin </b> y <b> Python </b>. <br>
    <br>
    <b> Postgres </b>, <b> Pgadmin </b> se implementaron para delimitar un espacio robusto en términos de seguridad e integridad referencial que permite el almacenamiento y manipulación de los datos. <br>
    <br>
    Mediante <b> Python </b> se realizó la extracción de los datos de fuentes gubernamentales del gobierno Argentino, a partir de la implementación de la librería <b> request </b> para  web-scraping. La limpieza y transformación de los datos se llevó a cabo haciendo uso de la librería <b> pandas </b>, para su posterior carga en la base datos. <br>
    <br>
    La conexión entre el motor de base de datos y <b> Python </b>  se estableció mediante un mapeador de objeto-relacional (<b>ORM</b>: Object-Relational mapping) llamado <b> SQLAlchemy </b> el cual se encuentra disponible como librería para este lenguaje de programación. La creación de las tablas se llevó a cabo a través de la ejecución de scripts .sql, los cuales son corridos desde <b> Python </b> mediante el <b> ORM</b>.  
    </p>
</body>

[<p style="font-family: rubik"> Índice </p> ](#id0)

---

<div id='id3' > </div>

<body>
    <h2> <b> Herramientas Utilizadas </b> </h2>
    <p>
        <ul>
            <li> <b> <p> 
            Docker
            </b>: La versión utilizada es la 3.8, los servicios de <b> Postgres </b>, <b> Pgadmin </b> son declarados directamente en el archivo .yml, el servicios de <b> Python </b> es construido a través de un Dockerfile.  </p> </li>
            <li> <b> <p> 
            Docker-compose
            </b>. </p> </li>           
            <li> <b> <p> 
            Postgres
            </b>: La versión utilizada es la 14.3.   </p> </li>
            <li> <b> <p> 
            Pgadmin
            </b>: La versión utilizada es la 6.11. </p> </li>
            <li> <b> <p> 
            Python
            </b>: La versión utilizada es la 3.10 </p> </li>
            <li> <b> <p> 
            Librerías
            </b>: 
                <ul>
                    <li> <p> Requests. </p> </li>
                    <li> <p> Bs4. </p> </li>
                    <li> <p> Python-decouple (módulo). </p> </li>
                    <li> <p> Logging (módulo). </p> </li>
                    <li> <p> SQLalchemy. </p> </li>
                    <li> <p> SQLalchemy Utils. </p> </li>
                    <li> <p> Pandas. </p> </li>
                    <li> <p> Psycopg2. </p> </li>
                    <li> <p> Pathlib (módulo). </p> </li>
                    <li> <p> Os (módulo). </p> </li>
                </ul>
            </p> </li>
        </ul>
    </p>
</body>

[<p style="font-family: rubik"> Índice </p> ](#id0)

---

<div id='id4' > </div>

<body>
    <h2> <b> Análisis Exploratorio de Datos</b> (EDA: Exploratory Data Analysis) </h2>
    <p>
    Para acceder al EDA haz clíck en:
    </p>
</body>

[<p style="font-family: rubik"> EDA </p>](eda.ipynb)

[<p style="font-family: rubik"> Índice </p> ](#id0)

---

<div id='id5' > </div>
 
<body>
    <h2> <b> Variables de Entorno </b> </h2>
    <p>
    El ETL cuenta con las siguientes variables de entorno:
    <ul>
        <li> <b> <p> 
        Configuración para Entorno de Python
        </b>. </p> </li>
        <ul>
            <li> <b> <p>
            DB_NAME
            </b>: < value > corresponde al nombre de la base de datos. </p> </li>
            <li> <b> <p>
            DB_USER
            </b>: < value > (credencial de acceso) corresponde al usuario de la base de datos. </p> </li>
            <li> <b> <p>
            DB_PASS
            </b>: < value > (credencial de acceso) corresponde a la contraseña de la base de datos. </p> </li>
            <li> <b> <p>
            DB_HOST
            </b>: "postgres" < default > red a través de la cual se establece la conexión con la base de datos. </p> </li>
            <li> <b> <p>
            DB_PORT
            </b>: "5432" < default > red a través de la cual "escucha" la base de datos. </p> </li>
            <li> <b> <p>
            MUSEO_URL
            </b>: < url_string > enlace de conexión a la fuente de datos. </p> </li>
            <li> <b> <p>
            CINE_URL
            </b>: < url_string > enlace de conexión a la fuente de datos. </p> </li>
            <li> <b> <p>
            BIBLIOTECA_URL
            </b>: < url_string > enlace de conexión a la fuente de datos. </p> </li>
        </ul>
    Estas variables pertmiten al <b> ORM </b> establecer la conexión entre Python y el motor de base de datos, deben ser especificadas en el archivo:
    </ul>   
</body>

[<p style="font-family: rubik"> Configuración para Entorno de Python </p>](./core_app/.env)

<body>  
    <ul>
    <li> <b> <p> 
    Configuración para los Servicios docker-compose.yml
    </b>. </p> </li>
        <ul>
            <li> <b> <p>
            POSTGRES_USER
            </b> < value > (credencial de acceso) corresponde al usuario de la base de datos. </p> </li>
            <li> <b> <p>
            POSTGRES_PASSWORD 
            </b> < value > (credencial de acceso) corresponde a la contraseña de la base de datos. </p> </li>
            <li> <b> <p>
            POSTGRES_PORT
            </b> el valor por defecto es <b> "5432"</b>. </p> </li>  
            <li> <b> <p>
            PGADMIN_PORT
            </b> el valor por defecto es <b> "5050"</b>. </p> </li>
            <li> <b> <p>
            PGADMIN_DEFAULT_EMAIL
            </b> el valor por defecto es <b> "pgadmin4@pgadmin.org"</b>. </p> </li>      
            <li> <b> <p>
            PGADMIN_DEFAULT_PASSWORD
            </b> el valor por defecto es <b> "admin"</b>. </p> </li>
        </ul>
        <p>
        Estás variables pertmiten a Docker Compose crear los servicios con Postgres (motor de base de datos) y Pgadmin (interfaz gráfica), deben ser especificadas en el archivo:
        </p>    
    </ul>
</body>

[<p style="font-family: rubik"> Archivo Docker Compose </p>](docker-compose.yml)

[<p style="font-family: rubik"> Índice </p> ](#id0)

---

<div id='id6' > </div>

<body>
    <h2> <b> Configuración del Motor de Base de Datos (Postgres) </b> </h2>
    <p>
    Para configurar el motor de base de datos se deben declarar las variables <b> POSTGRES_USER </b> y <b> POSTGRES_PASSWORD </b>, la variable <b> POSTGRES_PORT </b> está definida por defecto, se recomienda su modificación con discreción.
    </p>
</body>

[<p style="font-family: rubik"> Índice </p> ](#id0)

---

<div id='id7' > </div>

<body>
    <h2> <b> Configuración de la Conexión con  Postgres </b> </h2>
    <p>
    Para configurar la conexión entre Python y Postgres se deben declarar las variables <b> DB_NAME </b>, <b> DB_USER </b>, <b> DB_PASS </b>, <b> DB_HOST </b>, <b> DB_PORT </b>. <br>
    <br> 
    Las variables <b> DB_USER </b>, <b> DB_PASS </b> deben corresponder a los mismos parámetros definidos para <b> POSTGRES_USER </b> y <b> POSTGRES_PASSWORD </b>. <br>
    <br>
    Las variables <b> DB_HOST </b> y <b> DB_PORT </b> están definidas por defecto, se recomienda su modificación con discreción.
    <h3> <b> Acceso a Postgres </b> </h3>
    </p>
</body>

```
localhost: 5432
username: <value>
password: <value>
```

[<p style="font-family: rubik"> Índice </p> ](#id0)

---

<div id='id8' > </div>
    
<body>  
    <h2> <b> Configuración de la Interfaz Gráfica para la Base de Datos (Pgadmin4)</b> </h2>
    <p>
    Las variables <b> PGADMIN_DEFAULT_EMAIL </b>, <b> PGADMIN_DEFAULT_PASSWORD </b> están definidas por defecto, se recomienda su modificación con discreción.
    <h3> <b> Acceso a Pgadmin4 </b> </h3>
    </p>
</body>

```
URL: http://localhost:5050 (desde el navegador)
username: pgadmin4@pgadmin.org (por defecto)
password: admin (por defecto)
```

<body>  
    <h3> <b> Crear un Nuevo Servidor en Pgadmin4 </b> </h3>
</body>

```
Host name/address: postgres
Port: 5432
Username corresponde a POSTGRES_USER: <value>
Password corresponde a POSTGRES_PASSWORD: <value>
```

[<p style="font-family: rubik"> Índice </p> ](#id0)

---

<div id='id9' > </div>

<body>
    <h2> <b> Ejecución </b> </h2>
    <p>
    <ol>
        <li> <p> Clonar o descargar el repositorio. </p> </li>
        <li> <p> Abrir la terminal de comandos. </p> </li>
        <li> <p> Acceder al directorio <b> alkemy_challenge</b>. </p> </li>
        <li> <p> Ejecutar el comando <b> docker-compose build</b>. </p> </li> 
        <li> <p> Ejecutar el comando <b> docker-compose up -d</b>. </p> </li>        
    </ol>
    </p>
</body>

[<p style="font-family: rubik"> Índice </p> ](#id0)

---
