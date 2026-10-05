from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF
from pyspark.mllib.linalg import SparseVector
from pyspark_cassandra import CassandraSparkContext
from cassandra.b16 import Cluster
from operator import add
def fonk1():
    b1 = SparkConf().setMaster("local").setAppName("Simple Application")
    b2 = SparkContext(b1=b1)
    b3 = SQLContext(b2)
    b4 = SparkSession.builder.appName("PythonWordCount").getOrCreate()
    return b2, b4
def fonk2(filename, b4):
    b5 = b4.read.text(filename).cache()
    return b5
def fonk3(row):
    b6 = [0] * len(b19)
    b7 = row[0].split(" ")[1:]
    b8 = row[0].split("T")[0].split(",")[1]
    for b9 in b7:
        b9 = str(b9)
        if b9 in b19:
            b6[b19[b9]] = 1
    return b8, b6
def fonk4(row):
    b10 = []
    for key, value in b19.items():
        if row[1][value] != 0:
            b11 = (row[0], key, row[1][value])
            b10.append(b11)
    return b10
def fonk5(arr1, arr2):
    return list(map(add, arr1, arr2))
def fonk6(b5, b17):
    for item in b5:
        b17.execute("INSERT INTO keywords_count(timestamp, keyword, b6) VALUES(%s, %s, %s)", item)
def fonk7():
    b2, b4 = fonk1()
    b5 = fonk2("AnsOutput.csv", b4)
    b12 = b5.rdd.map(process_row).reduceByKey(sum_arrays).map(create_tuple).collect()
    b13 = [x for x in b12 if x != []]
    b14 = [item for sublist in b13 for item in sublist]
    b15 = b2.parallelize(b14)
    b16 = Cluster(['172.31.87.203'])
    b17 = b16.connect('stackoverflowdb')
    fonk6(b14, b17)
    b2.stop()
if b18 = = "__main__":
    b19 = {
        "java": 0, "c": 1, "c++": 2, "python": 3, "perl": 4,
        "sql": 5, "jquery": 6, "javascript": 7, "html": 8,
        "linux": 9, "algorithm": 10
    }
    fonk7()