#   Importamos las librerias
from decouple import AutoConfig
from constans import CORE_APP_DIR

#   Cargamos las varialbes de entorno
config = AutoConfig(search_path = CORE_APP_DIR)

db_name = config("DB_NAME")
db_user = config("DB_USER")
db_pass = config("DB_PASS")
db_host = config("DB_HOST")
db_port = config("DB_PORT")

#   Disponibilizamos las datasources
museo_dtsource = {
    "name": "museo",
    "url": config("MUSEO_URL")
}

cine_dtsource = {
    "name": "sala_cine",
    "url": config("CINE_URL")
}

biblio_dtsource = {
    "name": "biblioteca_popular",
    "url": config("BIBLIOTECA_URL")
}

#   Listamos las datasource
dict_list = [
    museo_dtsource,
    cine_dtsource,
    biblio_dtsource
]

