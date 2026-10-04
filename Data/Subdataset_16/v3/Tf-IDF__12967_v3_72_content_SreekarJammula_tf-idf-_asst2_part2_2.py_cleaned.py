from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def fonk1(context):
    file_path, b1 = context
    b2 = re.sub('[^a-z0-9]+', ' ', b1.lower()).split()
    b3 = file_path.split("/")[-1]
    return b3, b2
b4 = SparkConf().setAppName("part2_uni").set("b6.executor.memory", "2g")
b5 = SparkContext(b4=b4)
b6 = SparkSession(b5)
b7 = b5.wholeTextFiles("/cosc6339_s17/books-longlist/")
if hasattr(b7, "toDF"):
    b8 = b7.map(preprocess_text).toDF(["bookname", "b2"])
    b9 = NGram(n=2, inputCol="b2", outputCol="bigrams")
    b10 = b9.transform(b8)
    b11 = HashingTF(inputCol="bigrams", outputCol="bigram_tf")
    b12 = b11.transform(b10)
    b13 = IDF(inputCol="bigram_tf", outputCol="bigram_tf_idf")
    b14 = b13.fit(b12)
    b15 = b14.transform(b12)
    b15.rdd.saveAsTextFile("/bigd12/output2_2")
b5.stop()