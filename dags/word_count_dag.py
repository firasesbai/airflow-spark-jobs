from datetime import datetime

from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

spark_master = "spark://spark-master:7077"
input_path = "/usr/local/spark/data/ebook"

now = datetime.now()

with DAG(
    dag_id='spark_word_count',
    schedule_interval=None,
    start_date=datetime(now.year, now.month, now.day),
    catchup=False,
    tags=['spark']
) as dag:
    start = DummyOperator(task_id="start")

    spark_job = SparkSubmitOperator(
        application='/usr/local/spark/jobs/word_count_job.py',
        conn_id='spark_local',
        task_id='word_count',
        verbose=1,
        conf={"spark.master":spark_master, "job.local.dir":"/usr/local/spark/data/"},
        application_args=[input_path]
    )

    end = DummyOperator(task_id="end")

start >> spark_job >> end 
