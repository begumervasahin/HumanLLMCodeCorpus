from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def fonk1(b1):
    return re.sub('[^a-z0-9]+', ' ', b1.lower()).split()
def fonk2(file_path):
    return file_path.split("/")[-1]
def fonk3(file_path_content_pair):
    file_path, b1 = file_path_content_pair
    b2 = fonk1(b1)
    b3 = fonk2(file_path)
    return b3, b2
def fonk4(b4 = "part2_uni", executor_memory="2g"):
    b5 = SparkConf().setAppName(b4).set("b7.executor.memory", executor_memory)
    b6 = SparkContext(b5=b5)
    b7 = SparkSession(b6)
    return b6, b7
def fonk5(b16):
    b8 = NGram(n=1, inputCol="b2", outputCol="unigrams")
    b9 = b8.transform(b16)
    b10 = HashingTF(inputCol="unigrams", outputCol="unigram-tf")
    b11 = b10.transform(b9)
    b12 = IDF(inputCol="unigram-tf", outputCol="unigram-tf-idf")
    b13 = b12.fit(b11)
    b14 = b13.transform(b11)
    return b14
def fonk6():
    b6, b7 = fonk4()
    b15 = b6.wholeTextFiles("/cosc6339_s17/books-longlist/")
    if hasattr(b15, "toDF"):
        b16 = b15.map(process_file_content).toDF(["bookname", "b2"])
        b14 = fonk5(b16)
        b14.rdd.saveAsTextFile("/bigd12/output2_1")
    else:
        print("DataFrame support is not available. Please update your Spark installation.")
    b6.stop()
if b17 = = "__main__":
    fonk6()