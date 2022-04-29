import sys 
from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark import SparkFiles

APP_NAME = "WordCount"

if __name__ == '__main__':

    spark = SparkSession.builder.appName(APP_NAME).getOrCreate()
    sc = spark.sparkContext
    
    print("Application Initialized: " + APP_NAME)
    
    input_path = sys.argv[1]

    print("Reading text file from: %s", input_path)
    input_df = spark.read.text(input_path)

    print("Counting words...")
    # Convert to lowercase and remove special characters
    input_df_without_special_char = input_df.select(
        func.regexp_replace(func.lower(input_df.value), r'[\.,+-;"]', " ").alias("new_value"))
    # Split into words
    words = input_df_without_special_char.select(
        func.explode(func.split(input_df_without_special_char.new_value, " ")).alias("word"))
    # Remove empty words
    non_empty_ords = words.filter(words.word != "")
    # Count words' occurrences
    words_count = non_empty_ords.groupby("word").count().orderBy("word")

    print(words_count.show())
         
    print("Application Done: " + APP_NAME)
    spark.stop()
