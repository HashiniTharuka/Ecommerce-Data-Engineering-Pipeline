from datetime import datetime

from airflow.sdk import dag, task
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook


@dag(
    dag_id="ecommerce_snowflake_test_dag",
    schedule=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["ecommerce", "snowflake", "integration"]
)
def ecommerce_snowflake_test():

    @task
    def test_snowflake_connection():

        hook = SnowflakeHook(
            snowflake_conn_id="snowflake_conn"
        )

        sql = """
        -- Check the active Snowflake connection details.
        SELECT
            CURRENT_USER(),
            CURRENT_ROLE(),
            CURRENT_WAREHOUSE(),
            CURRENT_DATABASE(),
            CURRENT_SCHEMA()
        """

        result = hook.get_first(sql)

        print("SNOWFLAKE CONNECTION SUCCESSFUL")
        print("Connection details:", result)

    test_snowflake_connection()


ecommerce_snowflake_test()