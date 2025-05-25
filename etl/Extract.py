import pandas as pd

def extract_data(file_path):
    """
    Reads ride data from a CSV file and returns a DataFrame.
    
    Args: file_path (str): Path to the raw data CSV file.
        
    Returns: DataFrame: Raw ride data
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded {len(df)} rows from {file_path}")
        return df
    except Exception as e:
        print(f"Failed to load data: {e}")
        return None
