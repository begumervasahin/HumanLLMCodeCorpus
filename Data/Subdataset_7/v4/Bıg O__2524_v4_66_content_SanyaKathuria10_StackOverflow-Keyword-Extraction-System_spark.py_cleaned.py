from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF
from pyspark.mllib.linalg import SparseVector
from pyspark_cassandra import CassandraSparkContext
from cassandra.b17 import Cluster
from operator import add
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
def fonk2(list1):
    b11 = []
    for key, value in b6.items():
        if list1[1][value] != 0:
            b12 = (list1[0], key, list1[1][value])
            b11.append(b12)
    return b11
def fonk3(list1, list2):
    return list(map(add, list1, list2))
b13 = b5.rdd.map(process_row).reduceByKey(sum_arrays).map(create_tuple).collect()
b14 = [x for x in b13 if x != []]
b15 = [item for sublist in b14 for item in sublist]
b16 = b2.parallelize(b15)
b17 = Cluster(['172.31.87.203'])
b18 = b17.connect('stackoverflowdb')
for i in range(len(b15)):
    b18.execute("INSERT INTO keywords_count(timestamp, keyword, b7) VALUES(%s, %s, %s)", b15[i])
b2.stop()