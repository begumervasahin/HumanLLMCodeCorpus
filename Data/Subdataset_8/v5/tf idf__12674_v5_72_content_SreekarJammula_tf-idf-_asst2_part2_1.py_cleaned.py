from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def extract_words_from_text(text):
    return re.sub('[^a-z0-9]+', ' ', text.lower()).split()
def extract_file_name_and_words(file_content):
    file_path, text = file_content
    file_name = file_path.split("/")[-1]
    words = extract_words_from_text(text)
    return file_name, words
def configure_spark():
    conf = SparkConf().setAppName("Part 2 - Unigram").set("spark.executor.memory", "2g")
    return SparkContext(conf=conf)
def create_unigram_dataframe(files_rdd, spark_session):
    files_df = files_rdd.map(extract_file_name_and_words).toDF(["bookname", "words"])
    unigram_transformer = NGram(n=1, inputCol="words", outputCol="unigrams")
    return unigram_transformer.transform(files_df)
def calculate_tfidf(dataframe):
    hashing_tf = HashingTF(inputCol="unigrams", outputCol="unigram-tf")
    tf_df = hashing_tf.transform(dataframe)
    idf = IDF(inputCol="unigram-tf", outputCol="unigram-tf-idf")
    idf_model = idf.fit(tf_df)
    return idf_model.transform(tf_df)
def main():
    sc = configure_spark()
    spark = SparkSession(sc)
    files_rdd = sc.wholeTextFiles("/cosc6339_s17/books-longlist/")
    if hasattr(files_rdd, "toDF"):
        unigram_df = create_unigram_dataframe(files_rdd, spark)
        tfidf_df = calculate_tfidf(unigram_df)
        tfidf_df.rdd.saveAsTextFile("/bigd12/output2_1")
    else:
        print("Error: The RDD does not support the toDF conversion.")
if __name__ == "__main__":
    main()