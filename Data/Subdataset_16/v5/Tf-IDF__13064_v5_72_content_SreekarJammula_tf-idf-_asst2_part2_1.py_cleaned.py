from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def fonk1(context):
    file_path, b1 = context
    b2 = re.sub('[^a-z0-9]+', ' ', b1.lower()).split()
    b3 = file_path.split("/")[-1]
    return b3, b2
def fonk2():
    b4 = SparkConf().setAppName("part2_uni").set("b6.executor.memory", "2g")
    b5 = SparkContext(b4=b4)
    b6 = SparkSession(b5)
    b7 = b5.wholeTextFiles("/cosc6339_s17/books-longlist/")
    assert hasattr(b7, "toDF"), "RDD cannot be converted to DataFrame"
    b8 = b7.map(preprocess_text)
    b9 = b8.toDF(["bookname", "b2"])
    b10 = NGram(n=1, inputCol="b2", outputCol="unigrams")
    b11 = b10.transform(b9)
    b12 = HashingTF(inputCol="unigrams", outputCol="unigram_tf")
    b13 = b12.transform(b11)
    b14 = IDF(inputCol="unigram_tf", outputCol="unigram_tf_idf")
    b15 = b14.fit(b13)
    b16 = b15.transform(b13)
    b16.rdd.saveAsTextFile("/bigd12/output2_1")
    b5.stop()
if b17 = = "__main__":
    fonk2()