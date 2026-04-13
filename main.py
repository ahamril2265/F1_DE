# =========================
# main.py
# =========================
from ingestion import ingest_ergast, ingest_fastf1
from processing import clean_data, transform_data
from storage import load_to_postgres


def run_pipeline():
    ingest_ergast.run()
    ingest_fastf1.run()
    clean_data.run()
    transform_data.run()
    load_to_postgres.run()


if __name__ == '__main__':
    run_pipeline()