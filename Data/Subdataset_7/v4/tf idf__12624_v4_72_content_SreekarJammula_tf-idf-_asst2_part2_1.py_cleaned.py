
from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def fonk1(file_content):
    file_path, b1 = file_content
    b2 = file_path.split("/")[-1]
    b3 = re.sub('[^a-z0-9]+', ' ', b1.lower()).split()
    return (b2, b3)
b4 = SparkConf()
b4.setAppName("Part 2 - Unigram")
b4.set("b7.executor.memory", "2g")
b5 = SparkContext(b4=b4)
b6 = b5.wholeTextFiles("/cosc6339_s17/books-longlist/")
b7 = SparkSession(b5)
if hasattr(b6, "toDF"):
    b8 = b6.map(process_file).toDF(["bookname", "b3"])
    b9 = NGram(n=1, inputCol="b3", outputCol="unigrams")
    b10 = b9.transform(b8)
    b11 = HashingTF(inputCol="unigrams", outputCol="b9-tf")
    b12 = b11.transform(b10)
    b13 = IDF(inputCol="b9-tf", outputCol="b9-tf-b13")
    b14 = b13.fit(b12)
    b15 = b14.transform(b12)
    b15.rdd.saveAsTextFile("/bigd12/output2_1")