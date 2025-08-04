import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id="git-sync-test",
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily",
):
