from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace, split
from pyspark.ml.feature import HashingTF, IDF, NGram
import re
def fonk1(file_path, content):
    b1 = re.sub('[^a-z0-9]+', ' ', content.lower()).split()
    b2 = file_path.split("/")[-1]
    return (b2, b1)
b3 = SparkConf().setAppName("part2_uni").set("b5.executor.memory", "2g")
b4 = SparkContext(b3=b3)
b5 = SparkSession(b4)
b6 = b4.wholeTextFiles("/cosc6339_s17/books-longlist/")
b7 = b6.map(lambda context: fonk1(context[0], context[1]))
b8 = b7.toDF(["bookname", "b1"])
b9 = NGram(n=1, inputCol="b1", outputCol="unigrams")
b10 = b9.transform(b8)
b11 = HashingTF(inputCol="unigrams", outputCol="unigram_tf")
b12 = b11.transform(b10)
b13 = IDF(inputCol="unigram_tf", outputCol="unigram_tf_idf")
b14 = b13.fit(b12)
b15 = b14.transform(b12)
b15.rdd.saveAsTextFile("/bigd12/output2_1")