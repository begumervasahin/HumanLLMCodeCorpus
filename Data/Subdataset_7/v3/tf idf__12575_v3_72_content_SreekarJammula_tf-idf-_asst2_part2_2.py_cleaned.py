
from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def fonk1(file_path, content):
    b1 = re.sub('[^a-z0-9]+', ' ', content.lower()).split()
    b2 = file_path.split("/")[-1]
    return (b2, b1)
b3 = SparkConf().setAppName("TF-IDF for bigrams").set("b5.executor.memory", "2g")
b4 = SparkContext(b3=b3)
b5 = SparkSession(b4)
b6 = b4.wholeTextFiles("/cosc6339_s17/books-longlist/")
b7 = b6.map(lambda context: fonk1(*context)).toDF(["bookname", "b1"])
b8 = NGram(n=2, inputCol="b1", outputCol="bigrams")
b9 = b8.transform(b7)
b10 = HashingTF(inputCol="bigrams", outputCol="b8-tf")
b11 = b10.transform(b9)
b12 = IDF(inputCol="b8-tf", outputCol="b8-tf-b12")
b13 = b12.fit(b11)
b14 = b13.transform(b11)
b14.rdd.saveAsTextFile("/bigd12/output2_2")
b4.stop()