
from pyspark import SparkConf, SparkContext
from pyspark.ml.feature import HashingTF, IDF, NGram
from pyspark.sql import SparkSession
import re
def process_content(context):
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
    tokenized_df = lines.map(process_content).toDF(["bookname", "words"])
    unigram = NGram(n=1, inputCol="words", outputCol="unigrams")
    unigram_df = unigram.transform(tokenized_df)
    hashingTF = HashingTF(inputCol="unigrams", outputCol="unigram-tf")
    tf_data = hashingTF.transform(unigram_df)
    idf = IDF(inputCol="unigram-tf", outputCol="unigram-tf-idf")
    idf_model = idf.fit(tf_data)
    tfidf_result = idf_model.transform(tf_data)
    tfidf_result.rdd.saveAsTextFile("/bigd12/output2_1")
else:
    print("toDF method not available. Upgrade your Spark version.")
sc.stop()