import sqlite3
import pandas as pd
import time
from datetime import datetime, timedelta

# Load cleaned data from SQLite
conn = sqlite3.connect("data/rides.db")
df = pd.read_sql("SELECT * FROM fact_rides ORDER BY pickup_time", conn)
conn.close()

# Convert pickup_time to datetime
df["pickup_time"] = pd.to_datetime(df["pickup_time"])

# Rolling window: last 60 seconds
rolling_window = []

print("Starting real-time simulation... (1 trip/sec)\n")

for index, row in df.iterrows():
    current_time = datetime.now()

    # Append current trip to window
    rolling_window.append({
        "timestamp": current_time,
        "fare": row["fare_amount"]
    })

    # Remove entries older than 60 seconds
    rolling_window = [r for r in rolling_window if r["timestamp"] > current_time - timedelta(seconds=3600)]

    # Calculate rolling metrics
    trips_last_minute = len(rolling_window)
    avg_fare = round(sum(r["fare"] for r in rolling_window) / trips_last_minute, 2)

    # Print live stats
    print(f"[{current_time.strftime('%H:%M:%S')}] Trips in last 60s: {trips_last_minute} | Rolling Avg Fare: ₹{avg_fare}")

    time.sleep(1)

    if index == 100:  # Limit to 100 records for demo (remove to stream all)
        break
