<<<<<<< HEAD
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

import os 
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
=======
import os 
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from pipelines.reddit_pipeline import reddit_pipeline



>>>>>>> 833acef (fixing secrets)

default_args = {
    "owner": "abdelrahman",
    "start_date": datetime(2025, 4, 7),
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id="etl_reddit_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    tags=["reddit", "etl"]
)


# Extraction from reddit
extract = PythonOperator(
    task_id="reddit_extraction",
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
<<<<<<< HEAD
    }
)
=======
    },
    dag=dag
)

extract
>>>>>>> 833acef (fixing secrets)
