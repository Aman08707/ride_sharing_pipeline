from etl.Extract import extract_data
from etl.Transform import clean_data
from etl.Load import load_dataframe_to_sqlite, load_csv_to_sqlite
#from data_quality_check.data_quality import run_data_quality_checks
#from streaming import 

def main():
    db_path = "data/rides.db"
    print("Starting Ride-Sharing Data Pipeline...\n")

    # Step 1: Extract
    print("Step 1: Extracting data from raw_rides.csv")
    df_raw = extract_data("data/raw_rides.csv")

    # Step 2: Transform
    print("\n Step 2: Cleaning raw data")
    df_cleaned = clean_data(df_raw)

    # Step 3: Load cleaned data into SQLite
    print("\n Step 3: Loading cleaned rides into SQLite")
    db_path = "data/rides.db"
    load_dataframe_to_sqlite(df_cleaned, db_path, "fact_rides")

    # Step 4: Load driver dimension from CSV
    print("\n Step 4: Loading driver details into dim_drivers")
    load_csv_to_sqlite("data/raw_drivers.csv", db_path, "dim_drivers")

    print("\n Pipeline executed successfully!")


if __name__ == "__main__":
    main()
