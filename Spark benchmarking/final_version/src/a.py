import time

from pyspark.sql import SparkSession


def get_spark_session(app_name: str):
    return SparkSession.builder \
        .master('spark://spark-master:7077') \
        .appName(app_name) \
        .config('spark.executor.memory', '2g') \
        .getOrCreate()


if __name__ == '__main__':
    files = [(100, 50), (1000, 50), (10000, 50)]
    spark = get_spark_session("test")
    try:
        for num_rows, num_columns in files:
            path = f"/src/data/rows{num_rows}_columns{num_columns}.csv"
            df = spark.read.csv(path)
            df.show()
            time.sleep(10)
    except Exception:
        spark.stop()
