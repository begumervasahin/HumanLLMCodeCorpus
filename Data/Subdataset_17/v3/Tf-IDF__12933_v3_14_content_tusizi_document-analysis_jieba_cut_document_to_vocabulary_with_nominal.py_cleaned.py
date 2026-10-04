import json
import jieba.posseg as pseg
from pyspark import SparkContext
sc = SparkContext(appName='CutDocument')
ALLOWED_POS = {
    "n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng",
    "s", "f", "v", "vd", "vn", "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"
}
def cut(text):
    seg_list = list(pseg.cut(text))
    filtered_list = [word for word, flag in seg_list if flag in ALLOWED_POS]
    encoded_list = [word.encode("utf-8") for word in filtered_list]
    return encoded_list
def output(items):
    filename = "/vagrant/vocabulary/mominal.txt"
    joined_text = " ".join(items)
    with open(filename, "a+") as file:
        file.write(joined_text + "\n")
def filter_stopword(words, stop_words):
    return [word for word in words if word not in stop_words]
src_file = '/vagrant/data/data.txt'
stop_words_file = 'stop_words.txt'
rdd = sc.textFile(src_file).map(lambda x: json.loads(x)['content'])
stop_words_rdd = set(sc.textFile(stop_words_file).map(lambda x: x.encode("utf-8")).collect())
rdd.map(cut).map(lambda words: filter_stopword(words, stop_words_rdd)).foreach(output)