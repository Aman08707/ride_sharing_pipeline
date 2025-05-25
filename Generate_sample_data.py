import pandas as pd
import random as r
from faker import Faker as f
from datetime import datetime as dt, timedelta as td

# # Initialize Faker for generating names, cities, UUIDs
fake = f()

# # Store ride records
# rides = []

# # Get today's date
# today = dt.now()

# # Generate 2000 ride entries
# for _ in range(2000):
#     # Pick a random day in the past 30 days
#     days_ago = r.randint(0, 29)
#     ride_date = today - td(days=days_ago)

#     # Add random hour, minute to simulate hourly logs
#     pickup_time = ride_date.replace(
#         hour=r.randint(0, 23),
#         minute=r.randint(0, 59),
#         second=0,
#         microsecond=0
#     )

#     # Dropoff time is 5–60 minutes after pickup
#     dropoff_time = (pickup_time + td(minutes=r.randint(30, 120))).replace(second=0,microsecond=0)

#     # Create a ride record
#     ride = {
#         "trip_id": r.randint(1,2000) if r.random() > 0.01 else None,
#         "driver_id": r.randint(1, 20),
#         "pickup_time": pickup_time,
#         "dropoff_time": dropoff_time if r.random() > 0.02 else None,
#         "pickup_location": fake.city() if r.random() > 0.01 else None,
#         "fare_amount": round(r.uniform(100.0, 500.0), 2) if r.random() > 0.01 else None,
#         "status": r.choice(["Completed", "Cancelled", "In_Progress"])
#     }

#     rides.append(ride)

# # Convert to DataFrame
# df = pd.DataFrame(rides)

# #print(df)

# # Save to CSV
# df.to_csv("data/raw_rides.csv", index=False)

# print("Successfully generated 2000 ride records in data/raw_rides.csv")

drivers = []

for _ in range(20):
    drive = {
        "driver_id": r.randint(1, 20),
        "driver_name": fake.name_male()    }
    drivers.append(drive)

#Convert to DataFrame
drive_df =pd.DataFrame(drivers)

# Save to CSV
drive_df.to_csv("data/raw_drivers.csv", index=False)

print("Successfully generated 20 drivers records in data/raw_drivers.csv")