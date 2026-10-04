import json
import jieba.posseg as pseg
from pyspark import SparkContext
sc = SparkContext(appName='CutDocument')
ALLOWED_POS = [
    "n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng", "s",
    "f", "v", "vd", "vn", "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"
]
def cut(text):
    seg_list = list(pseg.cut(text))
    filtered_list = filter(lambda word_flag: word_flag.flag in ALLOWED_POS, seg_list)
    encoded_list = map(lambda word_flag: word_flag.word.encode("utf-8"), filtered_list)
    return list(encoded_list)
def output(items):
    filename = "/vagrant/vocabulary/nominal.txt"
    with open(filename, "a+") as fo:
        fo.write(" ".join(items) + "\n")
def filter_stopwords(words):
    return filter(lambda word: word not in stopWordList, words)
src_file = '/vagrant/data/data.txt'
rdd = sc.textFile(src_file).map(lambda x: json.loads(x)['content'])
stopWordList = sc.textFile("stop_words.txt").map(lambda x: x.encode("utf-8")).collect()
result = rdd.map(cut).map(filter_stopwords).foreach(output)