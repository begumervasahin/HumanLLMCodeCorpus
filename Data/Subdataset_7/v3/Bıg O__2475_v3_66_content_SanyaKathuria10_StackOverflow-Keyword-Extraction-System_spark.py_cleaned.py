from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession
from operator import add
from itertools import islice
from cassandra.b16 import Cluster
def fonk1():
    b1 = SparkConf().setMaster("local").setAppName("Simple Application")
    b2 = SparkContext(b1=b1)
    b3 = SQLContext(b2)
    b4 = SparkSession.builder.appName("PythonWordCount").getOrCreate()
    return b2, b4
def fonk2(b4, file_path):
    b5 = b4.read.text(file_path).cache()
    return b5
def fonk3():
    b6 = {
        "java": 0, "c": 1, "c++": 2, "python": 3, "perl": 4,
        "sql": 5, "jquery": 6, "javascript": 7, "html": 8,
        "linux": 9, "algorithm": 10
    }
    return b6
def fonk4(row, b6):
    b7 = [0] * len(b6)
    b8 = row[0].split(" ")[1:]
    b9 = row[0].split("T")[0].split(",")[1]
    for b10 in b8:
        b10 = str(b10)
        if b10 in b6:
            b7[b6[b10]] = 1
    return b9, b7
def fonk5(entry, b6):
    b11 = []
    for keyword, index in b6.items():
        if entry[1][index] != 0:
            b12 = (entry[0], keyword, entry[1][index])
            b11.append(b12)
    return b11
def fonk6(arr1, arr2):
    return list(map(add, arr1, arr2))
def fonk7(b5, b6):
    b13 = b5.rdd.map(lambda x: fonk4(x, b6)) \
                             .reduceByKey(sum_arrays) \
                             .map(lambda x: fonk5(x, b6)) \
                             .collect()
    b14 = [x for x in b13 if x != []]
    b15 = [item for sublist in b14 for item in sublist]
    return b15
def fonk8(b15):
    b16 = Cluster(['172.31.87.203'])
    b17 = b16.connect('stackoverflowdb')
    for item in b15:
        b17.execute("INSERT INTO keywords_count(timestamp, keyword, b7) VALUES (%s, %s, %s)", item)
def fonk9(b2):
    b2.stop()
def fonk10():
    b2, b4 = fonk1()
    b5 = fonk2(b4, "AnsOutput.csv")
    b6 = fonk3()
    b15 = fonk7(b5, b6)
    fonk8(b15)
    fonk9(b2)
if b18 = = "__main__":
    fonk10()