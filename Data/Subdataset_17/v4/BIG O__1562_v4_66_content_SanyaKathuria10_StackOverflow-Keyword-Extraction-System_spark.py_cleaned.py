from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession
from cassandra.cluster import Cluster
from operator import add
conf = SparkConf().setMaster("local").setAppName("Keyword Count Application")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()
data = spark.read.text("AnsOutput.csv").cache()
hashmap = {
    "java": 0, "c": 1, "c++": 2, "python": 3, "perl": 4, "sql": 5,
    "jquery": 6, "javascript": 7, "html": 8, "linux": 9, "algorithm": 10
}
def process_row(row):
    count = [0] * len(hashmap)
    data = row[0].split(" ")
    wordlist = data[1:]
    date = data[0].split("T")[0].split(",")[1]
    for word in wordlist:
        word = str(word)
        if word in hashmap:
            count[hashmap[word]] = 1
    return date, count
def create_tuples(entry):
    date, counts = entry
    return [(date, key, counts[value]) for key, value in hashmap.items() if counts[value] != 0]
def sum_counts(list1, list2):
    return list(map(add, list1, list2))
processed_data = data.rdd.map(process_row).reduceByKey(sum_counts).map(create_tuples).collect()
data_to_insert = [item for sublist in processed_data if sublist for item in sublist]
collection = sc.parallelize(data_to_insert)
cluster = Cluster(['172.31.87.203'])
session = cluster.connect('stackoverflowdb')
for entry in data_to_insert:
    session.execute("INSERT INTO keywords_count(timestamp, keyword, count) VALUES(%s, %s, %s)", entry)
sc.stop()