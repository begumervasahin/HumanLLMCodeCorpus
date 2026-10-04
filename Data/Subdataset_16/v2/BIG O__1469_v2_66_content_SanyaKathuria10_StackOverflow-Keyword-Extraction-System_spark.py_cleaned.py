from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession
from operator import add
from cassandra.b14 import Cluster
b1 = SparkConf().setMaster("local").setAppName("Keyword Count Application")
b2 = SparkContext(b1=b1)
b3 = SQLContext(b2)
b4 = SparkSession.builder.appName("PythonWordCount").getOrCreate()
b5 = {
    "java": 0, "c": 1, "c++": 2, "python": 3, "perl": 4,
    "sql": 5, "jquery": 6, "javascript": 7, "html": 8,
    "linux": 9, "algorithm": 10
}
def fonk1(row):
    b6 = [0] * len(b5)
    b7 = row[0].split(" ")
    b8 = b7[1:]
    b9 = b7[0].split("T")[0].split(",")[1]
    for b10 in b8:
        b10 = str(b10)
        if b10 in b5:
            b6[b5[b10]] = 1
    return b9, b6
def fonk2(row):
    b9, b11 = row
    b12 = [(b9, key, b11[value]) for key, value in b5.items() if b11[value] != 0]
    return b12
def fonk3(list1, list2):
    return list(map(add, list1, list2))
b7 = b4.read.text("AnsOutput.csv").cache()
b13 = b7.rdd.map(process_row).reduceByKey(sum_arrays).flatMap(create_tuples).collect()
b14 = Cluster(['172.31.87.203'])
b15 = b14.connect('stackoverflowdb')
for entry in b13:
    b15.execute(
        "INSERT INTO keywords_count (timestamp, keyword, b6) VALUES (%s, %s, %s)",
        entry
    )
b2.stop()