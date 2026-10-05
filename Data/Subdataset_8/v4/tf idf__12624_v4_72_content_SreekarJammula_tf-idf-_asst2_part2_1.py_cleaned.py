
from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def process_file(file_content):
    file_path, text = file_content
    file_name = file_path.split("/")[-1]
    words = re.sub('[^a-z0-9]+', ' ', text.lower()).split()
    return (file_name, words)
conf = SparkConf()
conf.setAppName("Part 2 - Unigram")
conf.set("spark.executor.memory", "2g")
sc = SparkContext(conf=conf)
files_rdd = sc.wholeTextFiles("/cosc6339_s17/books-longlist/")
spark = SparkSession(sc)
if hasattr(files_rdd, "toDF"):
    processed_files_df = files_rdd.map(process_file).toDF(["bookname", "words"])
    unigram = NGram(n=1, inputCol="words", outputCol="unigrams")
    unigram_df = unigram.transform(processed_files_df)
    hashingTF = HashingTF(inputCol="unigrams", outputCol="unigram-tf")
    tf_df = hashingTF.transform(unigram_df)
    idf = IDF(inputCol="unigram-tf", outputCol="unigram-tf-idf")
    idf_model = idf.fit(tf_df)
    tfidf_df = idf_model.transform(tf_df)
    tfidf_df.rdd.saveAsTextFile("/bigd12/output2_1")