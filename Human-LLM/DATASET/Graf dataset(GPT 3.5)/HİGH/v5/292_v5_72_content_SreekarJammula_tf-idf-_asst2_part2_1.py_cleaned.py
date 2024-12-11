from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def fonk1(b1):
    return re.sub('[^a-z0-9]+', ' ', b1.lower()).split()
def fonk2(file_content):
    file_path, b1 = file_content
    b2 = file_path.split("/")[-1]
    b3 = fonk1(b1)
    return b2, b3
def fonk3():
    b4 = SparkConf().setAppName("Part 2 - Unigram").set("b12.executor.memory", "2g")
    return SparkContext(b4 = b4)
def fonk4(b13, spark_session):
    b5 = b13.map(extract_file_name_and_words).toDF(["bookname", "b3"])
    b6 = NGram(n=1, inputCol="b3", outputCol="unigrams")
    return b6.transform(b5)
def fonk5(dataframe):
    b7 = HashingTF(inputCol="unigrams", outputCol="unigram-tf")
    b8 = b7.transform(dataframe)
    b9 = IDF(inputCol="unigram-tf", outputCol="unigram-tf-b9")
    b10 = b9.fit(b8)
    return b10.transform(b8)
def fonk6():
    b11 = fonk3()
    b12 = SparkSession(b11)
    b13 = b11.wholeTextFiles("/cosc6339_s17/books-longlist/")
    if hasattr(b13, "toDF"):
        b14 = fonk4(b13, b12)
        b15 = fonk5(b14)
        b15.rdd.saveAsTextFile("/bigd12/output2_1")
    else:
        print("Error: The RDD does not support the toDF conversion.")
if b16 = = "__main__":
    fonk6()