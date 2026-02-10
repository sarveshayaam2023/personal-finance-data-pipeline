from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("Hello from Airflow")

with DAG(
    dag_id="my_first_dag",
    start_date=datetime(2024, 2, 12),
    schedule=None,   # IMPORTANT for learning
    catchup=False
) as dag:

    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=say_hello
    )
