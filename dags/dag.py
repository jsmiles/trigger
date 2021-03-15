from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime


with DAG('python_dag', description='Python DAG', schedule_interval='*/5 * * * *', start_date=datetime(2018, 11, 1), catchup=False) as dag:
        pr1             = BashOperator(task_id='pr1', bash_command="python $AIRFLOW_HOME/dir/python/pr1.py")
        pr2             = BashOperator(task_id='pr2', bash_command="python $AIRFLOW_HOME/dir/python/pr2.py")
        pr3             = BashOperator(task_id='pr3', bash_command="python $AIRFLOW_HOME/dir/python/pr3.py")

        pr1 >> pr2 >> pr3
