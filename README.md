# F1 Data Engineering Pipeline

A comprehensive end-to-end data engineering pipeline designed to ingest, process, and visualize Formula 1 data. The project leverages modern data tools to pull data from APIs, clean and transform it, load it into a PostgreSQL database, and serve it via an interactive dashboard.

## Architecture & Components

1. **Ingestion**: 
   - Uses `fastf1` and Ergast API (`requests`) to pull telemetry, race, and driver data.
   - Scripts: `ingestion/ingest_ergast.py`, `ingestion/ingest_fastf1.py`
2. **Processing**: 
   - Cleans and transforms the raw data using `pandas` and `pyarrow`.
   - Scripts: `processing/clean_data.py`, `processing/transform_data.py`
3. **Storage**: 
   - Loads the processed data into a PostgreSQL database via `sqlalchemy` and `psycopg2`.
   - Script: `storage/load_to_postgres.py`
4. **Analytics & Dashboard**:
   - Analyzes data and visualizes it using a `Plotly Dash` web application.
   - Scripts: `analytics/queries.sql`, `dashboard/app.py`

## Prerequisites

- Python 3.9+
- Docker and Docker Compose (recommended for easy setup)
- PostgreSQL (if running locally without Docker)

## Setup & Execution

### 1. Environment Variables
Create a `.env` file in the root directory with your database credentials. E.g.:
```env
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=f1_db
```

### 2. Running with Docker (Recommended)
You can run the entire stack (Database, Pipeline, Dashboard) using Docker Compose:

```bash
docker-compose -f docker/docker-compose.yml up --build
```
- The dashboard will be available at `http://localhost:8050`
- The database will be exposed on port `5432`.

### 3. Running Locally (Without Docker)

1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

2. **Setup PostgreSQL**: Make sure a local PostgreSQL instance is running with the credentials specified in your `.env`.

3. **Run the Data Pipeline**:
Executes the ingestion, processing, and storage stages automatically.
```bash
python main.py
```

4. **Run the Dashboard**:
```bash
python dashboard/app.py
```
Open `http://localhost:8050` in your browser.

## Project Structure
```text
.
├── analytics/         # SQL queries and analytics scripts
├── cache/             # API data cache for FastF1
├── dashboard/         # Plotly Dash application
├── data/              # Local data storage/cache volumes
├── docker/            # Dockerfile and docker-compose.yml
├── ingestion/         # Data extraction scripts (Ergast, FastF1)
├── processing/        # Data cleaning and transformation scripts
├── storage/           # Database loading scripts
├── utils/             # Utility scripts containing configs and logger
├── Dashboard.pdf      # Dashboard preview/export
├── main.py            # Main entry point to run the pipeline
└── requirements.txt   # Python dependencies
```