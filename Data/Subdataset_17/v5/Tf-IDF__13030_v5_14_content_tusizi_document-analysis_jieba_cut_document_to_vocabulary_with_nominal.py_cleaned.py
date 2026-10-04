import json
import jieba.posseg as pseg
from pyspark import SparkContext
sc = SparkContext(appName='CutDocument')
ALLOWED_POS = {
    "n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng", "s",
    "f", "v", "vd", "vn", "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"
}
def cut(text):
    seg_list = pseg.cut(text)
    filtered_words = [word for word, flag in seg_list if flag in ALLOWED_POS]
    encoded_words = [word.encode("utf-8") for word in filtered_words]
    return encoded_words
def output(items):
    filename = "/vagrant/vocabulary/nominal.txt"
    with open(filename, "a+") as file:
        file.write(" ".join(items) + "\n")
def filter_stopwords(words):
    return [word for word in words if word not in stopWordList]
src_file = '/vagrant/data/data.txt'
rdd = sc.textFile(src_file).map(lambda x: json.loads(x)['content'])
stopWordList = sc.textFile("stop_words.txt").map(lambda x: x.encode("utf-8")).collect()
rdd.map(cut).map(filter_stopwords).foreach(output)