
from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def fonk1(context):
    file_path, b1 = context
    b2 = re.sub('[^a-z0-9]+', ' ', b1.lower()).split()
    b3 = file_path.split("/")[-1]
    return (b3, b2)
b4 = SparkConf()
b4.setAppName("TF-IDF for bigrams")
b4.set("b7.executor.memory", "2g")
b5 = SparkContext(b4=b4)
b6 = b5.wholeTextFiles("/cosc6339_s17/books-longlist/")
b7 = SparkSession(b5)
b8 = b6.map(process_file).toDF(["bookname", "b2"])
b9 = NGram(n=2, inputCol="b2", outputCol="bigrams")
b10 = b9.transform(b8)
b11 = HashingTF(inputCol="bigrams", outputCol="b9-tf")
b12 = b11.transform(b10)
b13 = IDF(inputCol="b9-tf", outputCol="b9-tf-b13")
b14 = b13.fit(b12)
b15 = b14.transform(b12)
b15.rdd.saveAsTextFile("/bigd12/output2_2")
b5.stop()