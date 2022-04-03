import logging

from pyspark.sql import SparkSession


def run(spark: SparkSession):
    logging.info("Hello Spark")
    spark.stop()
