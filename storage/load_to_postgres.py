from sqlalchemy import create_engine
import pandas as pd
import os
from utils.config import DB_URI, PROCESSED_DIR
import time
from sqlalchemy.exc import OperationalError

engine = create_engine(DB_URI)


def load_table(file, table):
    df = pd.read_parquet(os.path.join(PROCESSED_DIR, file))
    df.to_sql(table, engine, if_exists='replace', index=False)


def run():
    load_table("laps.parquet", "lap_times")
    load_table("driver_stats.parquet", "driver_stats")

def wait_for_db():
    for _ in range(10):
        try:
            engine = create_engine(DB_URI)
            conn = engine.connect()
            conn.close()
            print("DB connected")
            return engine
        except OperationalError:
            print("Waiting for DB...")
            time.sleep(3)
    raise Exception("DB not available")