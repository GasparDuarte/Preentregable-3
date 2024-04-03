from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from Preentrega3 import transform_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2022, 1, 1)
}

dag = DAG('transformacion_datos',
          default_args=default_args,
          description='Transformación de datos de criptomonedas',
          schedule_interval='@daily')

transform_data = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag
)
