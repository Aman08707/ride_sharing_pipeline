import sqlite3

def run_data_quality_checks(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    checks = {
        "Null trip_id": "SELECT COUNT(*) FROM fact_rides WHERE trip_id IS NULL",
        "Null fare_amount": "SELECT COUNT(*) FROM fact_rides WHERE fare_amount IS NULL",
        "Non-positive fares": "SELECT COUNT(*) FROM fact_rides WHERE fare_amount <= 0"
    }

    print("Running Data Quality Checks...\n")
    passed = True

    for check_name, query in checks.items():
        cursor.execute(query)
        count = cursor.fetchone()[0]
        if count > 0:
            print(f"{check_name}: {count} issue(s) found")
            passed = False
        else:
            print(f"{check_name}: OK")

    conn.close()

    if passed:
        print("\nAll data quality checks passed!")
    else:
        print("\nOne or more checks failed. Investigate before continuing.")

run_data_quality_checks("data/rides.db")