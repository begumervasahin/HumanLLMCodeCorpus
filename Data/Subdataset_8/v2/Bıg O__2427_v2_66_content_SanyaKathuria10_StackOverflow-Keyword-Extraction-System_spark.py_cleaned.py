from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession
from operator import add
from itertools import islice
from cassandra.cluster import Cluster
conf = SparkConf().setMaster("local").setAppName("Simple Application")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()
data = spark.read.text("AnsOutput.csv").cache()
keyword_map = {
    "java": 0, "c": 1, "c++": 2, "python": 3, "perl": 4,
    "sql": 5, "jquery": 6, "javascript": 7, "html": 8,
    "linux": 9, "algorithm": 10
}
def extract_keywords(row):
    count = [0] * len(keyword_map)
    word_list = row[0].split(" ")[1:]
    date = row[0].split("T")[0].split(",")[1]
    for word in word_list:
        word = str(word)
        if word in keyword_map:
            count[keyword_map[word]] = 1
    return date, count
def create_tuples(entry):
    temp = []
    for keyword, index in keyword_map.items():
        if entry[1][index] != 0:
            temp_tuple = (entry[0], keyword, entry[1][index])
            temp.append(temp_tuple)
    return temp
def sum_arrays(arr1, arr2):
    return list(map(add, arr1, arr2))
processed_data = data.rdd.map(extract_keywords).reduceByKey(sum_arrays).map(create_tuples).collect()
data_to_put = [x for x in processed_data if x != []]
flat_list = [item for sublist in data_to_put for item in sublist]
cluster = Cluster(['172.31.87.203'])
session = cluster.connect('stackoverflowdb')
for i in range(len(flat_list)):
    session.execute("INSERT INTO keywords_count(timestamp, keyword, count) VALUES (%s, %s, %s)", flat_list[i])
sc.stop()