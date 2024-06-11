from datetime import timedelta
from airflow import DAG
from airflow.operators import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from stock_etl import run_stock_etl

default_args = {
    'owner': 'bernard_airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 11),
    'email': ['iambenzeph@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'reddit_dag',
    default_args=default_args,
    description='GSE DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='complete_reddit_etl',
    python_callable=run_stock_etl,
    dag=dag, 
)

run_etl