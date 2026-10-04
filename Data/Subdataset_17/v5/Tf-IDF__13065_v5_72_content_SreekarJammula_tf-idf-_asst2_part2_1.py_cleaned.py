from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def preprocess_text(context):
    file_path, text = context
    words = re.sub('[^a-z0-9]+', ' ', text.lower()).split()
    file_name = file_path.split("/")[-1]
    return file_name, words
def main():
    conf = SparkConf().setAppName("part2_uni").set("spark.executor.memory", "2g")
    sc = SparkContext(conf=conf)
    spark = SparkSession(sc)
    lines = sc.wholeTextFiles("/cosc6339_s17/books-longlist/")
    assert hasattr(lines, "toDF"), "RDD cannot be converted to DataFrame"
    preprocessed_rdd = lines.map(preprocess_text)
    tokenized_df = preprocessed_rdd.toDF(["bookname", "words"])
    unigram = NGram(n=1, inputCol="words", outputCol="unigrams")
    unigram_df = unigram.transform(tokenized_df)
    hashing_tf = HashingTF(inputCol="unigrams", outputCol="unigram_tf")
    tf_df = hashing_tf.transform(unigram_df)
    idf = IDF(inputCol="unigram_tf", outputCol="unigram_tf_idf")
    idf_model = idf.fit(tf_df)
    tfidf_df = idf_model.transform(tf_df)
    tfidf_df.rdd.saveAsTextFile("/bigd12/output2_1")
    sc.stop()
if __name__ == "__main__":
    main()