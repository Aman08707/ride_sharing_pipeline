import sqlite3
import pandas as pd

conn = sqlite3.connect("data/rides.db")

# Average fare per hour
query1 = """
SELECT 
    STRFTIME('%H', pickup_time) AS pickup_hour,
    ROUND(AVG(fare_amount), 2) AS avg_fare
FROM fact_rides
GROUP BY pickup_hour
ORDER BY pickup_hour;
"""

# Total revenue per driver
query2 = """
SELECT 
    d.driver_id,
    d.driver_name,
    ROUND(SUM(f.fare_amount), 2) AS total_revenue
FROM fact_rides f
JOIN dim_drivers d ON f.driver_id = d.driver_id
GROUP BY d.driver_id, d.driver_name
ORDER BY total_revenue DESC;
"""

print("\n Average Fare Per Hour:")
print(pd.read_sql(query1, conn).to_string(index=False))

print("\n Total Revenue Per Driver:")
print(pd.read_sql(query2, conn).to_string(index=False))

conn.close()
