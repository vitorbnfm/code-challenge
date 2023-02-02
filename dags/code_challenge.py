from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta
from airflow.utils.dates import days_ago

default_args = {
   "owner": "Airflow",
   "depends_on_past": False,
   "start_date": days_ago(3),
   "retries": 1,
   }

with DAG(
   "code_challenge",
   schedule_interval=timedelta(days=1),
   default_args=default_args
   ) as dag:

   from_csv = BashOperator(
   task_id="from_csv",
   bash_command="""
   cd $AIRFLOW_HOME/dags/steps/
   python3 from_csv.py {{ execution_date }}
   """)

   from_postgres = BashOperator(
   task_id="from_postgres",
   bash_command="""
   cd $AIRFLOW_HOME/dags/steps/
   python3 from_postgres.py {{ execution_date }}
   """)

   to_database = BashOperator(
   task_id="to_database",
   bash_command="""
   cd $AIRFLOW_HOME/dags/steps/
   python3 to_database.py {{ execution_date }}
   """)



[from_csv, from_postgres] >> to_database 