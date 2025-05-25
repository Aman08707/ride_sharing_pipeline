import pandas as pd

def clean_data(df):
    """
    Cleans the raw ride data.
    
    Steps:
    - Drops rows with NULL trip_id, fare_amount, pickup_time, dropoff_time
    - Filters only 'completed' trips
    - Filters fare_amount > 0

    Args: df (DataFrame): Raw ride data

    Returns: DataFrame: Cleaned ride data
    """

    # Drop rows with missing key values
    df_cleaned = df.dropna(subset=['trip_id', 'fare_amount', 'pickup_time', 'dropoff_time'])

    # Filter only completed rides
    df_cleaned = df_cleaned[df_cleaned['status'] == 'Completed']

    # Filter out zero or negative fares
    df_cleaned = df_cleaned[df_cleaned['fare_amount'] > 0]

    print(f"Cleaned data: {len(df_cleaned)} rows remaining after cleaning.")
    return df_cleaned
