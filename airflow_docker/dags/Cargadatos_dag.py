from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from Preentrega3 import load_data_to_redshift

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 4, 2)
}

dag = DAG('carga_datos',
          default_args=default_args,
          description='Carga de datos de criptomonedas a Redshift',
          schedule_interval='@daily')

load_data = PythonOperator(
    task_id='load_data',
    python_callable=load_data_to_redshift,
    dag=dag
)
