﻿# Ride Sharing Pipeline
# Ride-Sharing Data Engineering Assignment

This project is a mini data engineering pipeline for a ride-sharing app. It includes batch data processing, star schema modeling, basic analytics, real-time simulation, and data quality checks.

---

## Project Features

- Generate mock ride and driver data
- ETL pipeline using Python and SQLite
- Star schema with fact and dimension tables
- SQL analytics: average fare per hour, total revenue per driver
- Real-time streaming simulation
- Data quality validation

---

## Tools Used

- Python
- pandas
- SQLite
- faker
- time
- timedelta

---

## How to Run

1. Clone the repo and set up a virtual environment
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Generate data:  
   `python Generate_sample_data.py`
4. Run ETL:  
   `python etl.py`
5. Run data quality checks:  
   `python data_quality_check/data_quality.py`
6. Simulate streaming:  
   `python streaming/stream.py`

---


