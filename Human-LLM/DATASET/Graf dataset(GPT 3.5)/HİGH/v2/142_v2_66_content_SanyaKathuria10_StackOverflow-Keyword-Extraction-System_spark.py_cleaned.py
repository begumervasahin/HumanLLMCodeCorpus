from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession
from operator import add
from itertools import islice
from cassandra.b16 import Cluster
b1 = SparkConf().setMaster("local").setAppName("Simple Application")
b2 = SparkContext(b1=b1)
b3 = SQLContext(b2)
b4 = SparkSession.builder.appName("PythonWordCount").getOrCreate()
b5 = b4.read.text("AnsOutput.csv").cache()
b6 = {
    "java": 0, "c": 1, "c++": 2, "python": 3, "perl": 4,
    "sql": 5, "jquery": 6, "javascript": 7, "html": 8,
    "linux": 9, "algorithm": 10
}
def fonk1(row):
    b7 = [0] * len(b6)
    b8 = row[0].split(" ")[1:]
    b9 = row[0].split("T")[0].split(",")[1]
    for b10 in b8:
        b10 = str(b10)
        if b10 in b6:
            b7[b6[b10]] = 1
    return b9, b7
def fonk2(entry):
    b11 = []
    for keyword, index in b6.items():
        if entry[1][index] != 0:
            b12 = (entry[0], keyword, entry[1][index])
            b11.append(b12)
    return b11
def fonk3(arr1, arr2):
    return list(map(add, arr1, arr2))
b13 = b5.rdd.map(extract_keywords).reduceByKey(sum_arrays).map(create_tuples).collect()
b14 = [x for x in b13 if x != []]
b15 = [item for sublist in b14 for item in sublist]
b16 = Cluster(['172.31.87.203'])
b17 = b16.connect('stackoverflowdb')
for i in range(len(b15)):
    b17.execute("INSERT INTO keywords_count(timestamp, keyword, b7) VALUES (%s, %s, %s)", b15[i])
b2.stop()