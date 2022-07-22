import logging
from constans import SCHEMA_NAME, SQL_SCRIPT_DIR, LOG_DIR
from confi import db_name, db_user, db_pass, db_host, db_port
from lets_connet import db_connetion
from sqlalchemy.sql import text
from datetime import datetime

"""
now = datetime.now()
year = now.year
month = now.month
day = now.day
date = f"{day:02d}-{month:02d}-{year}"
today_date = date.format(year = year, month = month, day = day)

logging.basicConfig(filename = f"{LOG_DIR}/app_run-{today_date}.log", level = "DEBUG")
"""

connetion = db_connetion(db_name, db_user, db_pass, db_host, db_port)
db, engine = connetion.start_connt()

def create_scheme(schema_name, engine):
    with engine.connect() as con:
        for table_leable in schema_name:
            print(f"Creating table: {table_leable}")
            logging.info(f"Creating table: {table_leable}")
            with open(f"{SQL_SCRIPT_DIR}/{table_leable}.sql") as scrtp:
                sql_query = text(scrtp.read())

            con.execute(sql_query)
            print(f"Done")
            logging.info("Done")
