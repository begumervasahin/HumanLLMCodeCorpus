from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def preprocess_text(context):
    file_path, text_content = context
    words = re.sub('[^a-z0-9]+', ' ', text_content.lower()).split()
    file_name = file_path.split("/")[-1]
    return file_name, words
conf = SparkConf().setAppName("part2_uni").set("spark.executor.memory", "2g")
sc = SparkContext(conf=conf)
spark = SparkSession(sc)
lines = sc.wholeTextFiles("/cosc6339_s17/books-longlist/")
if hasattr(lines, "toDF"):
    tokenized_df = lines.map(preprocess_text).toDF(["bookname", "words"])
    bigram_generator = NGram(n=2, inputCol="words", outputCol="bigrams")
    bigram_df = bigram_generator.transform(tokenized_df)
    hashing_tf = HashingTF(inputCol="bigrams", outputCol="bigram_tf")
    tf_df = hashing_tf.transform(bigram_df)
    idf = IDF(inputCol="bigram_tf", outputCol="bigram_tf_idf")
    idf_model = idf.fit(tf_df)
    tfidf_df = idf_model.transform(tf_df)
    tfidf_df.rdd.saveAsTextFile("/bigd12/output2_2")
sc.stop()