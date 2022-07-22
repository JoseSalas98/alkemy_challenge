#   Importamos la librerías
import requests
import pandas as pd
from pathlib import Path
from datetime import datetime
from constans import DATASET_DIR, OUT_DATASET_DIR


class dts_scraper:
    data_path = "{category}/{year}-{month:02d}/{category}-{day:02d}-{month:02d}-{year}.csv"
    main_path_ditc = {}

    def __init__(self, name, url):
        self.__name = name
        self.__url = url

    def get_scrap(self):
        now = datetime.now()
        category = self.__name
        year = now.year
        month = now.month
        day = now.day

        r = requests.get(self.__url)
        r.encoding = 'utf-8'
        fl_path = dts_scraper.data_path.format(category = category, year = year, 
                                                month = month, day = day)
        
        main_path = Path(f"{DATASET_DIR}/{fl_path}")
        main_path.parent.mkdir(parents=True,exist_ok=True)

        with open(main_path,'w') as file_outp:
            file_outp.write(r.text)
            file_name = "{category}-{day:02d}-{month:02d}-{year}.csv".format(category = category, 
                                                                            year = year, 
                                                                            month = month, 
                                                                            day = day)
            
            dts_scraper.main_path_ditc[self.__name] = f"{main_path}"
            print(f"Se ha guardado el archivo: {file_name} \nEn el directorio: {main_path} \n")

class dts_transform:
    def library_tranform(self, dts):
        df = dts

        columns = [
                    "Cod_Loc", 
                    "IdProvincia", 
                    "IdDepartamento", 
                    "Categoría", 
                    "Provincia", 
                    "Localidad", 
                    "Nombre", 
                    "Domicilio", 
                    "CP", 
                    "Teléfono", 
                    "Mail", 
                    "Web"
                    ]

        rename_columns = {
                            "Cod_Loc":"cod_localidad",
                            "IdProvincia":"id_provincia",
                            "IdDepartamento":"id_departamento",
                            "Categoría":"categoria",
                            "Provincia":"provincia",
                            "Localidad":"localidad",
                            "Nombre":"nombre",
                            "Domicilio":"domicilio",
                            "CP":"codigo_postal",
                            "Teléfono":"numero_de_telefono",
                            "Mail":"mail",
                            "Web":"web"
                            }
                            
        df = df[columns]
        df.rename(columns = rename_columns, inplace = True)

        return df

    def museum_tranform(seld, dts):
        df = dts

        columns = [
                    "Cod_Loc", 
                    "IdProvincia", 
                    "IdDepartamento", 
                    "categoria", 
                    "provincia", 
                    "localidad", 
                    "nombre", 
                    "direccion", 
                    "CP",
                    "telefono", 
                    "Mail", 
                    "Web"
                    ]

        rename_columns = {
                            "Cod_Loc":"cod_localidad", 
                            "IdProvincia":"id_provincia", 
                            "IdDepartamento":"id_departamento",
                            "categoria":"categoria", 
                            "provincia":"provincia", 
                            "localidad":"localidad", 
                            "nombre":"nombre", 
                            "direccion":"domicilio", 
                            "CP":"codigo_postal", 
                            "telefono":"numero_de_telefono", 
                            "Mail":"mail", 
                            "Web":"web"
                            }

        df = df[columns]
        df.rename(columns = rename_columns, inplace = True)

        return df
    
    def cine_tranform(self, dts):
        df= dts

        columns = [
                    "Cod_Loc", 
                    "IdProvincia", 
                    "IdDepartamento", 
                    "Categoría", 
                    "Provincia", 
                    "Localidad", 
                    "Nombre", 
                    "Dirección", 
                    "CP", 
                    "Teléfono", 
                    "Mail", 
                    "Web"
                    ]

        rename_columns = {
                            "Cod_Loc":"cod_localidad",
                            "IdProvincia":"id_provincia",
                            "IdDepartamento":"id_departamento",
                            "Categoría":"categoria",
                            "Provincia":"provincia",
                            "Localidad":"localidad",
                            "Nombre":"nombre",
                            "Dirección":"domicilio",
                            "CP":"codigo_postal",
                            "Teléfono":"numero_de_telefono",
                            "Mail":"mail",
                            "Web":"web"
                            }

        df = df[columns]
        df.rename(columns = rename_columns, inplace = True)

        return df

class dts_csv:
    def build_csv(self, schema_name):
        filepath = Path(f"{OUT_DATASET_DIR}/{schema_name}.csv")
        #filepath.parent.mkdir(parents=True, exist_ok=True)
        out_path = f"{filepath}"

        return out_path