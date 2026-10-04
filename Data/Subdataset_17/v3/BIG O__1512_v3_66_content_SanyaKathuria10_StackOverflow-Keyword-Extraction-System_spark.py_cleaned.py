from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession
from cassandra.cluster import Cluster
from operator import add
def initialize_spark(app_name="Keyword Count Application"):
    conf = SparkConf().setMaster("local").setAppName(app_name)
    sc = SparkContext(conf=conf)
    sql_context = SQLContext(sc)
    spark_session = SparkSession.builder.appName(app_name).getOrCreate()
    return sc, sql_context, spark_session
def define_keyword_map():
    return {
        "java": 0, "c": 1, "c++": 2, "python": 3, "perl": 4,
        "sql": 5, "jquery": 6, "javascript": 7, "html": 8,
        "linux": 9, "algorithm": 10
    }
def process_row(row, keyword_map):
    count = [0] * len(keyword_map)
    data = row[0].split(" ")
    wordlist = data[1:]
    date = data[0].split("T")[0].split(",")[1]
    for word in wordlist:
        if word in keyword_map:
            count[keyword_map[word]] = 1
    return date, count
def create_tuples(row, keyword_map):
    date, counts = row
    return [(date, key, counts[value]) for key, value in keyword_map.items() if counts[value] != 0]
def sum_arrays(list1, list2):
    return list(map(add, list1, list2))
def main():
    sc, sql_context, spark = initialize_spark()
    keyword_map = define_keyword_map()
    data = spark.read.text("AnsOutput.csv").cache()
    processed_data = (data.rdd
                      .map(lambda row: process_row(row, keyword_map))
                      .reduceByKey(sum_arrays)
                      .flatMap(lambda row: create_tuples(row, keyword_map))
                      .collect())
    cluster = Cluster(['172.31.87.203'])
    session = cluster.connect('stackoverflowdb')
    for entry in processed_data:
        session.execute(
            "INSERT INTO keywords_count (timestamp, keyword, count) VALUES (%s, %s, %s)",
            entry
        )
    sc.stop()
if __name__ == "__main__":
    main()