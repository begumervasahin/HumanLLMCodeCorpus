
from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def process_file(file_path, content):
    words = re.sub('[^a-z0-9]+', ' ', content.lower()).split()
    file_name = file_path.split("/")[-1]
    return (file_name, words)
conf = SparkConf().setAppName("TF-IDF for bigrams").set("spark.executor.memory", "2g")
sc = SparkContext(conf=conf)
spark = SparkSession(sc)
lines = sc.wholeTextFiles("/cosc6339_s17/books-longlist/")
tokenized_data = lines.map(lambda context: process_file(*context)).toDF(["bookname", "words"])
bigram = NGram(n=2, inputCol="words", outputCol="bigrams")
bigram_df = bigram.transform(tokenized_data)
hashingTF = HashingTF(inputCol="bigrams", outputCol="bigram-tf")
tf_data = hashingTF.transform(bigram_df)
idf = IDF(inputCol="bigram-tf", outputCol="bigram-tf-idf")
idf_model = idf.fit(tf_data)
tfidf_data = idf_model.transform(tf_data)
tfidf_data.rdd.saveAsTextFile("/bigd12/output2_2")
sc.stop()