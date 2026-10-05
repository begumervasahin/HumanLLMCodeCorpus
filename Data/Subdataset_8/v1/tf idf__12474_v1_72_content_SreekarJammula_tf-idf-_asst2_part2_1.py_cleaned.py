from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def part2(context):
    file_path, content = context
    words = re.sub('[^a-z0-9]+', ' ', content.lower()).split()
    file_name = file_path.split("/")[-1]
    return (file_name, words)
conf = SparkConf()
conf.setAppName("part2_uni")
conf.set("spark.executor.memory", "2g")
sc = SparkContext(conf=conf)
lines = sc.wholeTextFiles("/cosc6339_s17/books-longlist/")
spark = SparkSession(sc)
if hasattr(lines, "toDF"):
    tokenize = lines.map(part2).toDF(["bookname", "words"])
    unigram = NGram(n=1, inputCol="words", outputCol="unigrams")
    unigramdataframe = unigram.transform(tokenize)
    hashingTF = HashingTF(inputCol="unigrams", outputCol="unigram-tf")
    tf = hashingTF.transform(unigramdataframe)
    idf = IDF(inputCol="unigram-tf", outputCol="unigram-tf-idf")
    idfModel = idf.fit(tf)
    tfidfignore = idfModel.transform(tf)
    tfidfignore.rdd.saveAsTextFile("/bigd12/output2_1")
else:
    print("toDF method not available. Upgrade your Spark version.")
sc.stop()