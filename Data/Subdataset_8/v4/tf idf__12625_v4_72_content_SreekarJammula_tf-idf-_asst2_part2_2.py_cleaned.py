from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def process_file(context):
    file_path, text = context
    words = re.sub('[^a-z0-9]+', ' ', text.lower()).split()
    file_name = file_path.split("/")[-1]
    return (file_name, words)
conf = SparkConf()
conf.setAppName("TF-IDF Calculation")
conf.set("spark.executor.memory", "2g")
sc = SparkContext(conf=conf)
lines = sc.wholeTextFiles("/cosc6339_s17/books-longlist/")
spark = SparkSession(sc)
if hasattr(lines, "toDF"):
    tokenize = lines.map(process_file).toDF(["bookname", "words"])
    unigram = NGram(n=1, inputCol="words", outputCol="unigrams")
    unigram_df = unigram.transform(tokenize)
    hashingTF = HashingTF(inputCol="unigrams", outputCol="unigram-tf")
    tf = hashingTF.transform(unigram_df)
    idf = IDF(inputCol="unigram-tf", outputCol="unigram-tf-idf")
    idf_model = idf.fit(tf)
    tfidf_result = idf_model.transform(tf)
    tfidf_result.rdd.saveAsTextFile("/bigd12/output2_2")
else:
    print("toDF method not available in SparkContext")