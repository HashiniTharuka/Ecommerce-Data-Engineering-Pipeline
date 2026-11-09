
# E-commerce CSV Validation DAG
# Purpose: Validate Orders, Customers and Products CSV files.
# Expected rows: Orders = 8, Customers = 8, Products = 5.
# Tasks run in parallel after the start task.
# Retry settings: 2 retries with a 30-second delay.

import csv
from pathlib import Path
from datetime import datetime, timedelta

from airflow.sdk import dag, task

DATA_DIR = Path("/opt/airflow/data")


@dag(
    dag_id="ecommerce_csv_validation_dag",
    schedule=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["ecommerce", "csv-validation"]
)
def ecommerce_csv_validation():

    @task
    def start_pipeline():
        print("E-commerce CSV validation started")
        return "STARTED"

    @task(
        retries=2,
        retry_delay=timedelta(seconds=30)
    )
    def validate_csv(file_name, expected_columns, expected_rows, status):

        file_path = DATA_DIR / file_name

        if status != "STARTED":
            raise ValueError("Pipeline did not start correctly")

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            actual_columns = reader.fieldnames
            rows = list(reader)

        if actual_columns != expected_columns:
            raise ValueError(f"Invalid columns in {file_name}")

        if len(rows) != expected_rows:
            raise ValueError(
                f"Expected {expected_rows} rows, found {len(rows)}"
            )

        print(f"Dataset: {file_name}")
        print("Status: SUCCESS")
        print(f"Rows: {len(rows)}")
        print(f"Columns: {actual_columns}")

        return {
            "file": file_name,
            "status": "SUCCESS",
            "rows": len(rows)
        }

    @task
    def finish_pipeline(results):
        total_rows = sum(result["rows"] for result in results)

        print("ALL CSV VALIDATIONS COMPLETED")
        print("Total datasets:", len(results))
        print("Total rows:", total_rows)

    start = start_pipeline()

    # Intentional missing file to test Airflow retries.
    orders = validate_csv(
        "cleaned_orders.csv",
        [
            "order_id",
            "customer_id",
            "product_id",
            "quantity",
            "amount_lkr",
            "order_date"
        ],
        8,
        start
    )

    customers = validate_csv(
        "cleaned_customers.csv",
        [
            "customer_id",
            "customer_name",
            "email",
            "city"
        ],
        8,
        start
    )

    products = validate_csv(
        "products.csv",
        [
            "product_id",
            "product_name",
            "category",
            "unit_price_lkr"
        ],
        5,
        start
    )

    finish_pipeline([orders, customers, products])


ecommerce_csv_validation()
