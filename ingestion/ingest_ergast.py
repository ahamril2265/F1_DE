import requests
import pandas as pd
import os
from utils.config import RAW_DIR
from utils.logger import get_logger

logger = get_logger(__name__)
BASE_URL = "http://ergast.com/api/f1"


def fetch_endpoint(endpoint, filename):
    url = f"{BASE_URL}/{endpoint}.json?limit=1000"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            logger.error(f"Failed request {url}")
            return

        data = response.json()

        races = data.get('MRData', {}).get('RaceTable', {}).get('Races', [])

        if not races:
            logger.warning("No data found")
            return

        df = pd.json_normalize(races)

        os.makedirs(RAW_DIR, exist_ok=True)
        df.to_csv(os.path.join(RAW_DIR, f"{filename}.csv"), index=False)

        logger.info(f"{filename} saved successfully")

    except Exception as e:
        logger.error(f"Error: {e}")


# ✅ THIS FUNCTION MUST EXIST
def run():
    fetch_endpoint("2023", "races")