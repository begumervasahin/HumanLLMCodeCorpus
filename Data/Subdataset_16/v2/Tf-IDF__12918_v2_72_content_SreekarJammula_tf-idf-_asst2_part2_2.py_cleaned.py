from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def fonk1(context):
    b1 = context[0]
    b2 = context[1]
    b3 = re.sub('[^a-z0-9]+', ' ', b2.lower()).split()
    b4 = b1.split("/")[-1]
    return (b4, b3)
b5 = SparkConf().setAppName("part2_uni").set("b7.executor.memory", "2g")
b6 = SparkContext(b5=b5)
b7 = SparkSession(b6)
b8 = b6.wholeTextFiles("/cosc6339_s17/books-longlist/")
if hasattr(b8, "toDF"):
    b9 = b8.map(part2).toDF(["bookname", "b3"])
    b10 = NGram(n=2, inputCol="b3", outputCol="unigrams")
    b11 = b10.transform(b9)
    b12 = HashingTF(inputCol="unigrams", outputCol="unigram_tf")
    b13 = b12.transform(b11)
    b14 = IDF(inputCol="unigram_tf", outputCol="unigram_tf_idf")
    b15 = b14.fit(b13)
    b16 = b15.transform(b13)
    b16.rdd.saveAsTextFile("/bigd12/output2_2")
b6.stop()