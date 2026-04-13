import fastf1
import pandas as pd
import os
from utils.config import RAW_DIR
from utils.logger import get_logger
from utils.config import CACHE_DIR
os.makedirs(CACHE_DIR, exist_ok=True)
fastf1.Cache.enable_cache(CACHE_DIR)

logger = get_logger(__name__)

# Ensure cache directory exists
os.makedirs(CACHE_DIR, exist_ok=True)

fastf1.Cache.enable_cache(CACHE_DIR)


def run():
    session = fastf1.get_session(2023, 1, 'R')
    session.load()

    laps = session.laps
    laps.to_csv(os.path.join(RAW_DIR, "laps.csv"), index=False)
    logger.info("Saved lap data")