from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from Preentrega3 import get_top_10_crypto_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2022, 1, 1)
}

dag = DAG('extraccion_datos',
          default_args=default_args,
          description='Extracción de datos de criptomonedas',
          schedule_interval='@daily')

extract_data = PythonOperator(
    task_id='extract_data',
    python_callable=get_top_10_crypto_data,
    dag=dag
)
