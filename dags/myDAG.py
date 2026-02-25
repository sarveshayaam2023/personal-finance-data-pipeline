from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.ingestion import ingest_data
from src.cleaning import clean_data
from src.transformation import transform_data

with DAG(
    dag_id="finance_pipeline",
    start_date=datetime(2024, 2, 12),
    schedule=None,
    catchup=False
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest_data",
        python_callable=ingest_data
    )

    clean_task = PythonOperator(
        task_id="clean_data",
        python_callable=clean_data
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    ingest_task >> clean_task >> transform_task
