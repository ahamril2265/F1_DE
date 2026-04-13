import pandas as pd
import os
from utils.config import PROCESSED_DIR


def run():
    laps = pd.read_parquet(os.path.join(PROCESSED_DIR, "laps.parquet"))

    # ✅ Validate schema
    required_cols = ['driver', 'lapnumber', 'laptime']
    missing = [col for col in required_cols if col not in laps.columns]

    if missing:
        raise ValueError(f"Missing columns: {missing}. Found: {laps.columns}")

    # ✅ Convert laptime to seconds
    laps['laptime'] = pd.to_timedelta(laps['laptime'], errors='coerce')
    laps['lap_time_sec'] = laps['laptime'].dt.total_seconds()

    # ✅ 🔥 IMPORTANT — overwrite laps.parquet
    laps.to_parquet(os.path.join(PROCESSED_DIR, "laps.parquet"))

    # ✅ Aggregation
    agg = laps.groupby('driver')['lapnumber'].count().reset_index()
    agg.rename(columns={'lapnumber': 'lap_count'}, inplace=True)

    agg.to_parquet(os.path.join(PROCESSED_DIR, "driver_stats.parquet"))