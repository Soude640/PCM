from pyspark.sql import SparkSession


def get_spark_session(app_name: str):
    return SparkSession.builder \
        .master('spark://spark-master:7077') \
        .appName(app_name) \
        .getOrCreate()


if __name__ == '__main__':
    spark = get_spark_session("file")
    print(spark)
    sc = spark.sparkContext
    path = "/src/data/a.csv"
    df = spark.read.csv(path)
    df.show()
