from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession
from cassandra.b14 import Cluster
from operator import add
def fonk1(b1 = "Keyword Count Application"):
    b2 = SparkConf().setMaster("local").setAppName(b1)
    b3 = SparkContext(b2=b2)
    b4 = SQLContext(b3)
    b5 = SparkSession.builder.appName(b1).getOrCreate()
    return b3, b4, b5
def fonk2():
    return {
        "java": 0, "c": 1, "c++": 2, "python": 3, "perl": 4,
        "sql": 5, "jquery": 6, "javascript": 7, "html": 8,
        "linux": 9, "algorithm": 10
    }
def fonk3(row, b12):
    b6 = [0] * len(b12)
    b7 = row[0].split(" ")
    b8 = b7[1:]
    b9 = b7[0].split("T")[0].split(",")[1]
    for word in b8:
        if word in b12:
            b6[b12[word]] = 1
    return b9, b6
def fonk4(row, b12):
    b9, b10 = row
    return [(b9, key, b10[value]) for key, value in b12.items() if b10[value] != 0]
def fonk5(list1, list2):
    return list(map(add, list1, list2))
def fonk6():
    b3, b4, b11 = fonk1()
    b12 = fonk2()
    b7 = b11.read.text("AnsOutput.csv").cache()
    b13 = (b7.rdd
                      .map(lambda row: fonk3(row, b12))
                      .reduceByKey(sum_arrays)
                      .flatMap(lambda row: fonk4(row, b12))
                      .collect())
    b14 = Cluster(['172.31.87.203'])
    b15 = b14.connect('stackoverflowdb')
    for entry in b13:
        b15.execute(
            "INSERT INTO keywords_count (timestamp, keyword, b6) VALUES (%s, %s, %s)",
            entry
        )
    b3.stop()
if b16 = = "__main__":
    fonk6()