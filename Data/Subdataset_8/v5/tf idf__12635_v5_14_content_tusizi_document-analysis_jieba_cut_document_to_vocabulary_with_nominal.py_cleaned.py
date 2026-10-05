import json
import jieba.posseg as pseg
from pyspark import SparkContext
sc = SparkContext(appName='CutDocument')
def tokenize_and_filter(text):
    segmented_words = list(pseg.cut(text))
    allowed_tags = ["n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng", "s", "f",
                    "v", "vd", "vn", "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"]
    filtered_words = [word for word, flag in segmented_words if flag in allowed_tags]
    encoded_words = [word.encode("utf-8") for word in filtered_words]
    return encoded_words
def write_to_file(items):
    filename = "/vagrant/vocabulary/mominal.txt"
    joined_items = " ".join(items)
    with open(filename, "a+") as file:
        file.write(joined_items + "\n")
def filter_stopwords(words):
    return [word for word in words if word not in stop_words]
src_file = '/vagrant/data/data.txt'
text_rdd = sc.textFile(src_file).map(lambda x: json.loads(x)['content'])
stop_words = set(sc.textFile("stop_words.txt").map(lambda x: x.strip().encode("utf-8")).collect())
result = text_rdd.map(tokenize_and_filter).map(filter_stopwords).foreach(write_to_file)