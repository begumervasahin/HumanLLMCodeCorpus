import re
from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
def preprocess(context):
    file_path, content = context
    words = re.sub('[^a-z0-9]+', ' ', content.lower()).split()
    file_name = file_path.split("/")[-1]
    return file_name, words
conf = SparkConf().setAppName("part2_uni").set("spark.executor.memory", "2g")
sc = SparkContext(conf=conf)
lines = sc.wholeTextFiles("/cosc6339_s17/books-longlist/")
spark = SparkSession(sc)
assert hasattr(lines, "toDF"), "RDD does not have toDF method"
tokenized_df = lines.map(preprocess).toDF(["bookname", "words"])
ngram = NGram(n=2, inputCol="words", outputCol="unigrams")
unigram_df = ngram.transform(tokenized_df)
hashing_tf = HashingTF(inputCol="unigrams", outputCol="unigram_tf")
tf = hashing_tf.transform(unigram_df)
idf = IDF(inputCol="unigram_tf", outputCol="unigram_tf_idf")
idf_model = idf.fit(tf)
tfidf_df = idf_model.transform(tf)
tfidf_df.rdd.saveAsTextFile("/bigd12/output2_2")
sc.stop()