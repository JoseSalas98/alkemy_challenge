#   Importamos las librerias
import os
from pathlib import Path

#   Declaramos los directorios
MAIN_DIR = Path("../")
CORE_APP_DIR = Path(os.path.abspath(os.getcwd()))
SQL_SCRIPT_DIR = Path(f"{CORE_APP_DIR}/sql_script")
DATASET_DIR = Path(f"{MAIN_DIR}/dataset")
OUT_DATASET_DIR = Path(f"{DATASET_DIR}/out_dataset")
LOG_DIR = Path(f"{DATASET_DIR}/log")

#   Declaramos los nombres de las tablas
TABLE01 = "cultural_info"
TABLE02 = "cine_features"
TABLE03 = "size_datasource"
TABLE04 = "size_category"
TABLE05 = "size_cat_prov"

#   Creamos una lista con los esquemas a disponibilizar
SCHEMA_NAME = [
    TABLE01,
    TABLE02,
    TABLE03,
    TABLE04,
    TABLE05
]

