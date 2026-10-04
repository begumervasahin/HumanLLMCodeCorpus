import json
import jieba.posseg as pseg
from pyspark import SparkContext
sc = SparkContext(appName='CutDocument')
def cut(text):
    seg_list = pseg.cut(text)
    allowed_flags = {
        "n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng",
        "s", "f", "v", "vd", "vn", "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"
    }
    filtered_list = [word for word, flag in seg_list if flag in allowed_flags]
    return filtered_list
def output(items):
    filename = "/vagrant/vocabulary/mominal.txt"
    with open(filename, "a+", encoding="utf-8") as fo:
        fo.write(" ".join(items))
        fo.write("\n")
def filter_stopwords(tokens):
    return [token for token in tokens if token not in stopWordRdd]
stop_words_file = "stop_words.txt"
stopWordRdd = set(sc.textFile(stop_words_file).map(lambda x: x.strip()).collect())
src_file = '/vagrant/data/data.txt'
rdd = sc.textFile(src_file).map(lambda x: json.loads(x)['content'])
rdd.map(cut).map(filter_stopwords).foreach(output)
sc.stop()