import json
import jieba.posseg as pseg
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
b2 = [
    "n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng", "s",
    "f", "v", "vd", "vn", "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"
]
def fonk1(text):
    b3 = list(pseg.fonk1(text))
    b4 = filter(lambda word_flag: word_flag.flag in b2, b3)
    b5 = map(lambda word_flag: word_flag.word.encode("utf-8"), b4)
    return list(b5)
def fonk2(items):
    b6 = "/vagrant/vocabulary/nominal.txt"
    with open(b6, "a+") as fo:
        fo.write(" ".join(items) + "\n")
def fonk3(words):
    return filter(lambda word: word not in b9, words)
b7 = '/vagrant/data/data.txt'
b8 = b1.textFile(b7).map(lambda x: json.loads(x)['content'])
b9 = b1.textFile("stop_words.txt").map(lambda x: x.encode("utf-8")).collect()
b10 = b8.map(cut).map(filter_stopwords).foreach(output)