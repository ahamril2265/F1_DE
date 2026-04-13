FROM python:3.12-slim

WORKDIR /app

ENV PYTHONPATH=/app

# System deps
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (cache optimization)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy full project
COPY . .

# Create required folders
RUN mkdir -p data/raw data/processed cache

CMD ["python", "main.py"]