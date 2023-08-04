"""
demo_pipeline
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from astro import sql as aql
import pandas as pd
import pendulum


@aql.dataframe(task_id="python_1")
def python_1_func():
    print("executed task 1")

@aql.dataframe(task_id="python_2")
def python_2_func():
    print("executed task 2")

@dag(
    schedule="0 0 * * *",
    start_date=pendulum.from_format("2023-08-04", "YYYY-MM-DD").in_tz("UTC"),
    catchup=False,
)
def demo_pipeline():
    python_1 = python_1_func()

    python_2 = python_2_func()

    python_2 << python_1

dag_obj = demo_pipeline()