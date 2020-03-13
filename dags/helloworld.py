## Credit to https://github.com/vishalsatam/Data-Pipelining/blob/master/Airflow/AirflowDemo/Helloworld.py

from airflow import DAG
from airflow.operators import BashOperator, PythonOperator
from datetime import datetime, timedelta


def print_hello_world():
    print('this_should_print_hello_world from python')


# Following are defaults which can be overridden later on
default_args = {
    'owner': 'Jackie G',
    'depends_on_past': False,
    'start_date': datetime(2016, 4, 15),
    'email': ['jackies-email'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('Helloworld', default_args=default_args)

t1 = BashOperator(
    task_id='hello_from_bash',
    bash_command='echo "Task 1 says hello"',
    dag=dag)

t2 = PythonOperator(
    task_id='hello_from_python',
    python_callable=print_hello_world,
    dag=dag)

t2.set_upstream(t1)
