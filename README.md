# 🏎️ Real-Time Formula 1 Data Engineering Pipeline

## 📌 Overview

This project is a **production-grade end-to-end Data Engineering pipeline** that ingests, processes, stores, and visualizes Formula 1 race data for **race strategy analytics**.

It integrates multiple data sources and provides an **interactive dashboard** for analyzing lap performance, driver behavior, and race dynamics.

---

## 🚀 Features

### 🔹 Data Ingestion

* Fetches historical race data from the **Ergast API**
* Extracts telemetry and lap-level data using **FastF1**
* Stores raw data in CSV format

### 🔹 Data Processing

* Cleans missing values and removes duplicates
* Standardizes schema and column naming
* Converts lap times into numerical format (seconds)
* Generates derived metrics:

  * Lap time trends
  * Driver lap counts
  * Performance indicators

### 🔹 Data Storage

* Uses **PostgreSQL** for structured storage
* Stores processed data in optimized **Parquet format**
* Automatically loads transformed data into database tables

### 🔹 Analytics Layer

* SQL queries for:

  * Fastest laps
  * Driver consistency
  * Performance comparison

### 🔹 Interactive Dashboard

Built using **Plotly Dash**:

* 📈 Lap time trends
* 🏎️ Position changes
* 📊 Average lap time comparison
* 🎯 Fastest lap insights
* 🎛️ Driver filters and lap range selection

---

## 🏗️ Architecture

```
Raw Data → Cleaning → Transformation → Storage → Dashboard
   ↓           ↓            ↓            ↓           ↓
 CSV       Parquet     Metrics     PostgreSQL    Plotly Dash
```

---

## 🧰 Tech Stack

| Layer            | Technology             |
| ---------------- | ---------------------- |
| Language         | Python                 |
| Data Processing  | Pandas                 |
| Data Source      | Ergast API, FastF1     |
| Storage          | PostgreSQL             |
| File Format      | CSV, Parquet           |
| Visualization    | Plotly Dash            |
| Containerization | Docker, Docker Compose |

---

## 📁 Project Structure

```
project_root/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── ingestion/
├── processing/
├── storage/
├── analytics/
├── dashboard/
├── utils/
│
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 🔹 1. Clone Repository

```
git clone <your-repo-url>
cd F1_DE
```

---

### 🔹 2. Configure Environment

Create `.env` file:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=f1db
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

---

### 🔹 3. Run with Docker (Recommended)

```
cd docker
docker compose up --build
```

---

## 🌐 Access Services

| Service    | URL                   |
| ---------- | --------------------- |
| Dashboard  | http://localhost:8050 |
| PostgreSQL | localhost:5432        |

---

## 📊 Dashboard Capabilities

* Multi-driver comparison
* Lap-by-lap performance tracking
* Race position visualization
* Fastest lap detection
* Interactive filtering

---

## 🧠 Key Engineering Concepts Demonstrated

* Modular pipeline design
* Schema validation and transformation
* Data lake simulation using filesystem
* Containerized multi-service architecture
* Fault-tolerant data ingestion
* Real-time-ready pipeline design

---

## ⚠️ Known Considerations

* Ergast API may occasionally return empty responses
* FastF1 data requires caching for efficiency
* Dashboard depends on successful data load into PostgreSQL

---

## 🔥 Future Enhancements

* Apache Kafka for real-time streaming
* Apache Airflow for orchestration
* dbt for transformation modeling
* Machine Learning for race strategy prediction
* Kubernetes deployment

---

## 👨‍💻 Author

**ARM**
Data Engineering & Full Stack Enthusiast

---

## ⭐ If you found this useful

Give it a ⭐ on GitHub and feel free to contribute!
