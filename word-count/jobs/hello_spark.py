import logging

from pyspark.sql import SparkSession
from transformations_basic import hello_spark

LOG_FILENAME = 'project.log'
APP_NAME = "WordCount"


if __name__ == '__main__':
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)

    spark = SparkSession.builder.appName(APP_NAME).getOrCreate()
    hello_spark.run(spark)
