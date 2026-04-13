import pandas as pd
import os
from utils.config import RAW_DIR, PROCESSED_DIR
from utils.logger import get_logger

logger = get_logger(__name__)


def clean_csv(file):
    df = pd.read_csv(os.path.join(RAW_DIR, file))
    df = df.drop_duplicates()
    df = df.ffill()  # ✅ updated (no deprecation warning)
    df.columns = [c.lower().replace(".", "_") for c in df.columns]
    return df


def run():
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    for file in os.listdir(RAW_DIR):
        path = os.path.join(RAW_DIR, file)

        # ✅ CRITICAL FIX — skip directories
        if not os.path.isfile(path):
            logger.warning(f"Skipping directory: {file}")
            continue

        # ✅ Only process CSV files
        if not file.endswith(".csv"):
            logger.warning(f"Skipping non-CSV file: {file}")
            continue

        df = clean_csv(file)

        out = os.path.join(PROCESSED_DIR, file.replace('.csv', '.parquet'))
        df.to_parquet(out)

        logger.info(f"Processed {file}")