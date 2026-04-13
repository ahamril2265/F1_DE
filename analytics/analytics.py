from sqlalchemy import create_engine
import pandas as pd
from utils.config import DB_URI

engine = create_engine(DB_URI)


def fastest_laps():
    query = "SELECT driver, MIN(lap_time_sec) as fastest FROM lap_times GROUP BY driver"
    return pd.read_sql(query, engine)