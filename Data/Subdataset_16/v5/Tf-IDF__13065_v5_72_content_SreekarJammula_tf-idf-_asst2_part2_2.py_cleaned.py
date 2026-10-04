import re
from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
def fonk1(context):
    file_path, b1 = context
    b2 = re.sub('[^a-z0-9]+', ' ', b1.lower()).split()
    b3 = file_path.split("/")[-1]
    return b3, b2
def fonk2():
    b4 = SparkConf().setAppName("part2_uni").set("b6.executor.memory", "2g")
    b5 = SparkContext(b4=b4)
    try:
        b6 = SparkSession(b5)
        b7 = b5.wholeTextFiles("/cosc6339_s17/books-longlist/")
        assert hasattr(b7, "toDF"), "RDD does not have toDF method"
        b8 = b7.map(preprocess).toDF(["bookname", "b2"])
        b9 = NGram(n=2, inputCol="b2", outputCol="unigrams")
        b10 = b9.transform(b8)
        b11 = HashingTF(inputCol="unigrams", outputCol="unigram_tf")
        b12 = b11.transform(b10)
        b13 = IDF(inputCol="unigram_tf", outputCol="unigram_tf_idf")
        b14 = b13.fit(b12)
        b15 = b14.transform(b12)
        b15.rdd.saveAsTextFile("/bigd12/output2_2")
    finally:
        b5.stop()
if b16 = = "__main__":
    fonk2()