import pandas as pd
import logging
from confi import dict_list, db_name, db_user, db_pass, db_host, db_port
from constans import SCHEMA_NAME, LOG_DIR
from lets_scrap import dts_scraper, dts_transform, dts_csv
from lets_connet import db_connetion
from datetime import datetime
from db_connect_script import create_scheme

now = datetime.now()
year = now.year
month = now.month
day = now.day
date = f"{day:02d}-{month:02d}-{year}"
today_date = date.format(year = year, month = month, day = day)

logging.basicConfig(filename = f"{LOG_DIR}/app_run-{today_date}.log", level = "DEBUG")

logging.info("Creating db connetion")
connetion = db_connetion(db_name, db_user, db_pass, db_host, db_port)
db, engine = connetion.start_connt()
logging.info("Done")

def extraction():
    
    for i in (dict_list):
        logging.info(f"Extracting datasource: {i}")
        dts = dts_scraper(name = i["name"], url = i["url"])
        dts.get_scrap()
        logging.info("Done")
    return dts

def transformation():

    df_dict = {}
    transform = dts_transform()

    for i in (dict_list):
        path = dts_scraper.main_path_ditc[i["name"]]
        df = pd.read_csv(filepath_or_buffer = path)
        logging.info(f"Transforming df: {i}")

        if ((i["name"]) == "museo"):
            df = transform.museum_tranform(dts=df)
            df_dict[i["name"]] = df

        elif ((i["name"]) == "sala_cine"):
            cine_df = df.copy()
            logging.info(f"cine_df saved")
            df = transform.cine_tranform(dts=df)
            df_dict[i["name"]] = df

        elif ((i["name"]) == "biblioteca_popular"):
            df = transform.library_tranform(dts=df)
            df_dict[i["name"]] = df
        logging.info("Done")

    merged_df = pd.concat(df_dict, axis = 0, ignore_index=True)
    logging.info(f"merged_df saved")
    logging.info(f"df_dict saved")
    
    return  merged_df, cine_df, df_dict

def get_insight():

    out_path_dict = {}
    get_csv = dts_csv()

    for i in (SCHEMA_NAME):
        if (i == "cultural_info"):
            cultural_info_df = merged_df.copy()
            out_path_dict[i] = get_csv.build_csv(schema_name = i)
            path = out_path_dict[i]
            cultural_info_df.to_csv(path_or_buf = path, index=False) 

        elif (i == "cine_features"):
            columns = [
                        "Provincia", 
                        "Pantallas", 
                        "Butacas", 
                        "espacio_INCAA"
                        ]
            cine_features_df = cine_df.groupby("Provincia", as_index=False).count()[columns]
            out_path_dict[i] = get_csv.build_csv(schema_name = i)
            path = out_path_dict[i]
            cine_features_df.to_csv(path_or_buf = path, index=False) 

        elif (i == "size_datasource"):
            lst = list()

            for name, df in df_dict.items():
                lst.append({"source": name, "count":df.size})
                
            size_datasource_df = pd.DataFrame(lst)
            out_path_dict[i] = get_csv.build_csv(schema_name = i)
            path = out_path_dict[i]
            size_datasource_df.to_csv(path_or_buf = path, index=False) 

        elif (i == "size_category"):
            size_category_df = merged_df.groupby(["categoria"], as_index=False).size()
            out_path_dict[i] = get_csv.build_csv(schema_name = i)
            path = out_path_dict[i]
            size_category_df.to_csv(path_or_buf = path, index=False) 

        elif (i == "size_cat_prov"):
            size_cat_prov_df = merged_df.groupby(["categoria", "provincia"], as_index=False).size()
            out_path_dict[i] = get_csv.build_csv(schema_name = i)
            path = out_path_dict[i]
            size_cat_prov_df.to_csv(path_or_buf = path, index=False) 

    return out_path_dict

def to_database():

    for i in SCHEMA_NAME:
        logging.info(f"Loading {i}_df to {db_name} table {i}")
        path = out_path_dict[i]
        df = pd.read_csv(filepath_or_buffer = path)
        df.to_sql(name = i, con = engine, if_exists = 'append', index = False)
        logging.info("Done")


dts = extraction()
merged_df, cine_df, df_dict = transformation()
out_path_dict = get_insight()


if __name__ == '__main__':
    create_scheme(schema_name = SCHEMA_NAME, engine = engine)
    to_database()
    connetion = connetion.end_connt()