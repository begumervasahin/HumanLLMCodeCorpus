from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
from operator import add
import re
import sys
def fonk1(context):
    b1 = context[0]
    b2 = re.sub('[^a-z0-9]+',' ',context[1].lower()).split()
    b1 = b1.split("/")[-1]
    return (b1,b2)
b3 = SparkConf()
b3.setAppName( "part2_uni" )
b3.set("b6.executor.memory", "2g")
b4 = SparkContext(b3 = b3)
b5 = b4.wholeTextFiles("/cosc6339_s17/books-longlist/")
b6 = SparkSession(b4)
hasattr(b5, "toDF")
b7 = b5.map(part2).toDF(["bookname", "b2"])
b8 = NGram(n=1, inputCol = "b2", outputCol = "unigrams")
b9 = b8.transform(b7)
b10 = HashingTF(inputCol = "unigrams", outputCol = "b8-b11")
b11 = b10.transform(b9)
b12 = IDF(inputCol = "b8-b11", outputCol = "b8-b11-b12")
b13 = b12.fit(b11)
b14 = b13.transform(b11)
b14.rdd.saveAsTextFile("/bigd12/output2_1")