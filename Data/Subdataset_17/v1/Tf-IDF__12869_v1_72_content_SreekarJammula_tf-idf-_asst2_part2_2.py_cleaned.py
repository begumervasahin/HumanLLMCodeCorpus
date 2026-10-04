from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def part2(context):
    file = context[0]
    words = re.sub('[^a-z0-9]+', ' ', context[1].lower()).split()
    file = file.split("/")[-1]
    return (file, words)
conf = SparkConf().setAppName("part2_uni").set("spark.executor.memory", "2g")
sc = SparkContext(conf=conf)
spark = SparkSession(sc)
lines = sc.wholeTextFiles("/cosc6339_s17/books-longlist/")
if hasattr(lines, "toDF"):
    tokenize = lines.map(part2).toDF(["bookname", "words"])
    unigram = NGram(n=2, inputCol="words", outputCol="unigrams")
    unigramdataframe = unigram.transform(tokenize)
    hashingTF = HashingTF(inputCol="unigrams", outputCol="unigram-tf")
    tf = hashingTF.transform(unigramdataframe)
    idf = IDF(inputCol="unigram-tf", outputCol="unigram-tf-idf")
    idfModel = idf.fit(tf)
    tfidf = idfModel.transform(tf)
    tfidf.rdd.saveAsTextFile("/bigd12/output2_2")
sc.stop()