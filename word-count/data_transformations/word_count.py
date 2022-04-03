import logging

from pyspark.sql import SparkSession
from pyspark.sql import functions as func


def run(spark: SparkSession, input_path: str, output_path: str) -> None:
    logging.info("Reading text file from: %s", input_path)
    input_df = spark.read.text(input_path)

    logging.info("Counting words...")
    # Convert to lowercase and remove special characters
    input_df_without_special_char = input_df.select(
        func.regexp_replace(func.lower(input_df.value), r'[\.,+-;"]', " ").alias("new_value"))
    # input_df_without_special_char = input_df.select(
    #     func.translate(func.lower(input_df.value), '.,-;"', " ").alias("new_value"))
    # Split into words
    words = input_df_without_special_char.select(
        func.explode(func.split(input_df_without_special_char.new_value, " ")).alias("word"))
    # Remove empty words
    non_empty_ords = words.filter(words.word != "")
    # Count words' occurrences
    words_count = non_empty_ords.groupby("word").count().orderBy("word")

    logging.info("Writing csv to directory: %s", output_path)
    words_count.coalesce(1).write.csv(output_path, header=True)
