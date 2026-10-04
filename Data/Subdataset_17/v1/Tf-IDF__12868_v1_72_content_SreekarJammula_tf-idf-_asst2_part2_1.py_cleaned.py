from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace, split
from pyspark.ml.feature import HashingTF, IDF, NGram
def preprocess(file_path, content):
    words = re.sub('[^a-z0-9]+', ' ', content.lower()).split()
    file_name = file_path.split("/")[-1]
    return (file_name, words)
conf = SparkConf().setAppName("part2_uni").set("spark.executor.memory", "2g")
sc = SparkContext(conf=conf)
spark = SparkSession(sc)
lines = sc.wholeTextFiles("/cosc6339_s17/books-longlist/")
preprocessed_rdd = lines.map(lambda context: preprocess(context[0], context[1]))
preprocessed_df = preprocessed_rdd.toDF(["bookname", "words"])
unigram = NGram(n=1, inputCol="words", outputCol="unigrams")
unigram_df = unigram.transform(preprocessed_df)
hashingTF = HashingTF(inputCol="unigrams", outputCol="unigram_tf")
tf_df = hashingTF.transform(unigram_df)
idf = IDF(inputCol="unigram_tf", outputCol="unigram_tf_idf")
idf_model = idf.fit(tf_df)
tfidf_df = idf_model.transform(tf_df)
tfidf_df.rdd.saveAsTextFile("/bigd12/output2_1")