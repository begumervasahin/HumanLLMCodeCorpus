from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def clean_and_split_content(content):
    return re.sub('[^a-z0-9]+', ' ', content.lower()).split()
def extract_file_name(file_path):
    return file_path.split("/")[-1]
def process_file_content(file_path_content_pair):
    file_path, content = file_path_content_pair
    words = clean_and_split_content(content)
    file_name = extract_file_name(file_path)
    return file_name, words
def configure_spark(app_name="part2_uni", executor_memory="2g"):
    conf = SparkConf().setAppName(app_name).set("spark.executor.memory", executor_memory)
    sc = SparkContext(conf=conf)
    spark = SparkSession(sc)
    return sc, spark
def transform_data_to_tfidf(tokenized_df):
    unigram_transformer = NGram(n=1, inputCol="words", outputCol="unigrams")
    unigram_df = unigram_transformer.transform(tokenized_df)
    hashing_tf_transformer = HashingTF(inputCol="unigrams", outputCol="unigram-tf")
    tf_data = hashing_tf_transformer.transform(unigram_df)
    idf_transformer = IDF(inputCol="unigram-tf", outputCol="unigram-tf-idf")
    idf_model = idf_transformer.fit(tf_data)
    tfidf_result = idf_model.transform(tf_data)
    return tfidf_result
def main():
    sc, spark = configure_spark()
    file_content_rdd = sc.wholeTextFiles("/cosc6339_s17/books-longlist/")
    if hasattr(file_content_rdd, "toDF"):
        tokenized_df = file_content_rdd.map(process_file_content).toDF(["bookname", "words"])
        tfidf_result = transform_data_to_tfidf(tokenized_df)
        tfidf_result.rdd.saveAsTextFile("/bigd12/output2_1")
    else:
        print("DataFrame support is not available. Please update your Spark installation.")
    sc.stop()
if __name__ == "__main__":
    main()