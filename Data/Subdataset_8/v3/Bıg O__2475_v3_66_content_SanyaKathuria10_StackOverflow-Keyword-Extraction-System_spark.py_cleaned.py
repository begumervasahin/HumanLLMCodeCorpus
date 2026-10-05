from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession
from operator import add
from itertools import islice
from cassandra.cluster import Cluster
def setup_spark():
    conf = SparkConf().setMaster("local").setAppName("Simple Application")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()
    return sc, spark
def read_csv(spark, file_path):
    data = spark.read.text(file_path).cache()
    return data
def define_keyword_map():
    keyword_map = {
        "java": 0, "c": 1, "c++": 2, "python": 3, "perl": 4,
        "sql": 5, "jquery": 6, "javascript": 7, "html": 8,
        "linux": 9, "algorithm": 10
    }
    return keyword_map
def extract_keywords(row, keyword_map):
    count = [0] * len(keyword_map)
    word_list = row[0].split(" ")[1:]
    date = row[0].split("T")[0].split(",")[1]
    for word in word_list:
        word = str(word)
        if word in keyword_map:
            count[keyword_map[word]] = 1
    return date, count
def create_tuples(entry, keyword_map):
    temp = []
    for keyword, index in keyword_map.items():
        if entry[1][index] != 0:
            temp_tuple = (entry[0], keyword, entry[1][index])
            temp.append(temp_tuple)
    return temp
def sum_arrays(arr1, arr2):
    return list(map(add, arr1, arr2))
def process_data(data, keyword_map):
    processed_data = data.rdd.map(lambda x: extract_keywords(x, keyword_map)) \
                             .reduceByKey(sum_arrays) \
                             .map(lambda x: create_tuples(x, keyword_map)) \
                             .collect()
    data_to_put = [x for x in processed_data if x != []]
    flat_list = [item for sublist in data_to_put for item in sublist]
    return flat_list
def write_to_cassandra(flat_list):
    cluster = Cluster(['172.31.87.203'])
    session = cluster.connect('stackoverflowdb')
    for item in flat_list:
        session.execute("INSERT INTO keywords_count(timestamp, keyword, count) VALUES (%s, %s, %s)", item)
def stop_spark(sc):
    sc.stop()
def main():
    sc, spark = setup_spark()
    data = read_csv(spark, "AnsOutput.csv")
    keyword_map = define_keyword_map()
    flat_list = process_data(data, keyword_map)
    write_to_cassandra(flat_list)
    stop_spark(sc)
if __name__ == "__main__":
    main()