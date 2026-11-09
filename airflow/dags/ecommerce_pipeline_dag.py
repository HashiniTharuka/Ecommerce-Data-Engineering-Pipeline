# E-commerce Data Pipeline DAG
# This DAG demonstrates task orchestration in Apache Airflow.
# Task order: Start -> Validate -> Finish.

from datetime import datetime
from airflow.sdk import dag, task


@dag(
    dag_id="ecommerce_pipeline_dag",
    schedule=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["ecommerce", "data-engineering"]
)
def ecommerce_pipeline():

    @task
    def start_pipeline():
        print("E-commerce pipeline started")
        return "STARTED"

    @task
    def validate_pipeline(status):
        print("Pipeline status:", status)
        print("Validating pipeline execution...")
        return "VALIDATION_SUCCESS"

    @task
    def finish_pipeline(validation_status):
        print("Validation:", validation_status)
        print("E-commerce pipeline completed successfully!")

    start = start_pipeline()
    validation = validate_pipeline(start)
    finish_pipeline(validation)


ecommerce_pipeline()