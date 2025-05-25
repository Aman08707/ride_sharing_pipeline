import sqlite3
import pandas as pd

"""
    Loads the cleaned DataFrame into a SQLite database.

    Args:
        df (DataFrame): Cleaned ride data
        csv_path: driver csv path
        db_path (str): Path to SQLite DB file
        table_name (str): Table name to write to
    """

def load_dataframe_to_sqlite(df, db_path, table_name):
    """Loads a given DataFrame to SQLite table."""
    try:
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        print(f"Loaded DataFrame into '{table_name}' in '{db_path}'")
    except Exception as e:
        print(f"Failed to load {table_name}: {e}")


def load_csv_to_sqlite(csv_path, db_path, table_name):
    """Loads a CSV file directly into a SQLite table."""
    try:
        driver_df = pd.read_csv(csv_path)
        load_dataframe_to_sqlite(driver_df, db_path, table_name)
        #print(f"Loaded csv into '{table_name}' in '{db_path}'")
    except Exception as e:
        print(f"Failed to load CSV '{csv_path}' to table '{table_name}': {e}")
