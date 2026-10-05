from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row, SparkSession
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF
from pyspark.mllib.linalg import SparseVector
import sys
from operator import add
import pandas as pd
from pyspark.sql import functions as F
from itertools import islice
import pyspark_cassandra
from pyspark_cassandra import CassandraSparkContext
from cassandra.b18 import Cluster
b1 = SparkConf().setMaster("local").setAppName("Simple Application")
b2 = SparkContext(b1= b1)
b3 = SQLContext(b2)
b4 = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()
b5 = b4.read.text("AnsOutput.csv").cache()
import unicodedata
b6 = {"java":0,"c":1, "c++":2, "python":3,"perl":4,"sql":5,"jquery":6,"javascript":7,"html":8,"linux":9,"algorithm":10}
def fonk1(row):
    b7 = [0] * len(b6)
    print row
    b8 = []
    b5 = row[0].split(" ")
    b8 = b5[1:]
    b9 = b5[0].split("T")[0].split(",")[1]
    print b8
    b10 = list()
    for b11 in b8:
	b11 = str(b11)
	if b11 in b6:
            b7[b6[b11]] = 1
    return b9,b7
def fonk2(list1):
   b12 = []
   print list1
   for key,value in b6.items():
	if list1[1][value]!=0:
	  b13 = (list1[0],key,list1[1][value])
	  b12.append(b13)
   return b12
def fonk3(list1,list2):
   return list(map(add, list1, list2))
b14 = b5.rdd.map(someFunction).reduceByKey(sumArrays).map(tupleCreate).collect()
print b14
b15 = [x for x in b14 if x!=[]]
print b15
b16 = [item for sublist in b15 for item in sublist]
print b16
print type(b16)
b17 = b2.parallelize(b16)
print b17
b18 = Cluster(['172.31.87.203'])
b19 = b18.connect('stackoverflowdb')
for i in range(len(b16)):
	b19.execute("INSERT INTO keywords_count(timestamp, keyword, b7) VALUES(%s, %s,  %s)", b16[i])
b2.stop()