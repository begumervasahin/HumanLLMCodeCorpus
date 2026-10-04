from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession
from cassandra.b15 import Cluster
from operator import add
b1 = SparkConf().setMaster("local").setAppName("Keyword Count Application")
b2 = SparkContext(b1=b1)
b3 = SQLContext(b2)
b4 = SparkSession.builder.appName("PythonWordCount").getOrCreate()
b5 = b4.read.text("AnsOutput.csv").cache()
b6 = {
    "java": 0, "c": 1, "c++": 2, "python": 3, "perl": 4, "sql": 5,
    "jquery": 6, "javascript": 7, "html": 8, "linux": 9, "algorithm": 10
}
def fonk1(row):
    b7 = [0] * len(b6)
    b5 = row[0].split(" ")
    b8 = b5[1:]
    b9 = b5[0].split("T")[0].split(",")[1]
    for b10 in b8:
        b10 = str(b10)
        if b10 in b6:
            b7[b6[b10]] = 1
    return b9, b7
def fonk2(entry):
    b9, b11 = entry
    return [(b9, key, b11[value]) for key, value in b6.items() if b11[value] != 0]
def fonk3(list1, list2):
    return list(map(add, list1, list2))
b12 = b5.rdd.map(process_row).reduceByKey(sum_counts).map(create_tuples).collect()
b13 = [item for sublist in b12 if sublist for item in sublist]
b14 = b2.parallelize(b13)
b15 = Cluster(['172.31.87.203'])
b16 = b15.connect('stackoverflowdb')
for entry in b13:
    b16.execute("INSERT INTO keywords_count(timestamp, keyword, b7) VALUES(%s, %s, %s)", entry)
b2.stop()