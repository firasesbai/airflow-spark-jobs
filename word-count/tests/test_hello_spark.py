from pyspark.sql import SparkSession


SPARK = SparkSession.builder.appName("Tests").getOrCreate()


def test_spark_can_be_run():
    assert "Tests" == SPARK.sparkContext.appName
