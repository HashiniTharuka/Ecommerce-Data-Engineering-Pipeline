
# E-commerce Snowflake Load DAG
# Purpose: Load Customers, Products and Orders CSV files into Snowflake.
# Uses MERGE to prevent duplicate records.
# Final step validates Snowflake table row counts.

import csv
from pathlib import Path
from datetime import datetime

from airflow.sdk import dag, task
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook

DATA_DIR = Path("/opt/airflow/data")
SNOWFLAKE_CONN_ID = "snowflake_conn"


def load_csv_to_snowflake(
    file_name,
    expected_columns,
    expected_rows,
    value_fields,
    merge_sql
):
    file_path = DATA_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != expected_columns:
            raise ValueError(f"Invalid columns in {file_name}")

        rows = [
            tuple(row[field] for field in value_fields)
            for row in reader
        ]

    if len(rows) != expected_rows:
        raise ValueError(
            f"Expected {expected_rows} rows in {file_name}, "
            f"found {len(rows)}"
        )

    hook = SnowflakeHook(snowflake_conn_id=SNOWFLAKE_CONN_ID)
    connection = hook.get_conn()

    try:
        with connection.cursor() as cursor:
            cursor.executemany(merge_sql, rows)

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()

    print(f"Loaded {len(rows)} records from {file_name}")

    return len(rows)


@dag(
    dag_id="ecommerce_snowflake_load_dag",
    schedule=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["ecommerce", "snowflake", "data-loading"]
)
def ecommerce_snowflake_load():

    @task
    def load_customers():

        # Insert new customers or update existing customers.
        sql = """
        MERGE INTO ECOMMERCE_DB.RAW_DATA.CUSTOMERS AS target
        USING (
            SELECT
                %s::INT AS CUSTOMER_ID,
                %s::VARCHAR AS CUSTOMER_NAME,
                %s::VARCHAR AS EMAIL,
                %s::VARCHAR AS CITY
        ) AS source
        ON target.CUSTOMER_ID = source.CUSTOMER_ID

        WHEN MATCHED THEN UPDATE SET
            CUSTOMER_NAME = source.CUSTOMER_NAME,
            EMAIL = source.EMAIL,
            CITY = source.CITY

        WHEN NOT MATCHED THEN INSERT (
            CUSTOMER_ID, CUSTOMER_NAME, EMAIL, CITY
        )
        VALUES (
            source.CUSTOMER_ID, source.CUSTOMER_NAME,
            source.EMAIL, source.CITY
        )
        """

        return load_csv_to_snowflake(
            "cleaned_customers.csv",
            ["customer_id", "customer_name", "email", "city"],
            8,
            ["customer_id", "customer_name", "email", "city"],
            sql
        )

    @task
    def load_products():

        # Insert new products or update existing products.
        sql = """
        MERGE INTO ECOMMERCE_DB.RAW_DATA.PRODUCTS AS target
        USING (
            SELECT
                %s::INT AS PRODUCT_ID,
                %s::VARCHAR AS PRODUCT_NAME,
                %s::VARCHAR AS CATEGORY,
                %s::NUMBER(10,2) AS UNIT_PRICE_LKR
        ) AS source
        ON target.PRODUCT_ID = source.PRODUCT_ID

        WHEN MATCHED THEN UPDATE SET
            PRODUCT_NAME = source.PRODUCT_NAME,
            CATEGORY = source.CATEGORY,
            UNIT_PRICE_LKR = source.UNIT_PRICE_LKR

        WHEN NOT MATCHED THEN INSERT (
            PRODUCT_ID, PRODUCT_NAME, CATEGORY, UNIT_PRICE_LKR
        )
        VALUES (
            source.PRODUCT_ID, source.PRODUCT_NAME,
            source.CATEGORY, source.UNIT_PRICE_LKR
        )
        """

        return load_csv_to_snowflake(
            "products.csv",
            ["product_id", "product_name", "category", "unit_price_lkr"],
            5,
            ["product_id", "product_name", "category", "unit_price_lkr"],
            sql
        )

    @task
    def load_orders():

        # Insert new orders or update existing orders.
        sql = """
        MERGE INTO ECOMMERCE_DB.RAW_DATA.ORDERS AS target
        USING (
            SELECT
                %s::INT AS ORDER_ID,
                %s::INT AS CUSTOMER_ID,
                %s::INT AS PRODUCT_ID,
                %s::INT AS QUANTITY,
                %s::NUMBER(12,2) AS AMOUNT_LKR,
                %s::DATE AS ORDER_DATE
        ) AS source
        ON target.ORDER_ID = source.ORDER_ID

        WHEN MATCHED THEN UPDATE SET
            CUSTOMER_ID = source.CUSTOMER_ID,
            PRODUCT_ID = source.PRODUCT_ID,
            QUANTITY = source.QUANTITY,
            AMOUNT_LKR = source.AMOUNT_LKR,
            ORDER_DATE = source.ORDER_DATE

        WHEN NOT MATCHED THEN INSERT (
            ORDER_ID, CUSTOMER_ID, PRODUCT_ID,
            QUANTITY, AMOUNT_LKR, ORDER_DATE
        )
        VALUES (
            source.ORDER_ID, source.CUSTOMER_ID,
            source.PRODUCT_ID, source.QUANTITY,
            source.AMOUNT_LKR, source.ORDER_DATE
        )
        """

        return load_csv_to_snowflake(
            "cleaned_orders.csv",
            [
                "order_id", "customer_id", "product_id",
                "quantity", "amount_lkr", "order_date"
            ],
            8,
            [
                "order_id", "customer_id", "product_id",
                "quantity", "amount_lkr", "order_date"
            ],
            sql
        )

    @task
    def validate_snowflake_counts(load_results):

        # Confirm that all three Snowflake tables contain expected rows.
        hook = SnowflakeHook(snowflake_conn_id=SNOWFLAKE_CONN_ID)

        expected_counts = {
            "CUSTOMERS": 8,
            "PRODUCTS": 5,
            "ORDERS": 8
        }

        total_rows = 0

        for table, expected in expected_counts.items():

            sql = f"""
            -- Count records in the loaded Snowflake table.
            SELECT COUNT(*)
            FROM ECOMMERCE_DB.RAW_DATA.{table}
            """

            result = hook.get_first(sql)
            actual = result[0]

            print(f"Table: {table}")
            print(f"Expected rows: {expected}")
            print(f"Actual rows: {actual}")

            if actual != expected:
                raise ValueError(
                    f"{table} count mismatch: expected {expected}, "
                    f"found {actual}"
                )

            total_rows += actual

        print("SNOWFLAKE DATA LOAD SUCCESSFUL")
        print("Total records:", total_rows)
        print("All three tables validated successfully.")

    customers = load_customers()
    products = load_products()
    orders = load_orders()

    validate_snowflake_counts([customers, products, orders])


ecommerce_snowflake_load()
