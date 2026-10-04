import json
import jieba.posseg as pseg
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
def fonk1(text):
    b2 = list(pseg.fonk1(text))
    b3 = {"n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng", "s", "f", "v", "vd", "vn", "vf",
                   "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"}
    b4 = [word for word, flag in b2 if flag in b3]
    b5 = [word.encode("utf-8") for word in b4]
    return b5
def fonk2(items):
    b6 = "/vagrant/vocabulary/mominal.txt"
    b7 = " ".b7(items)
    with open(b6, "a+") as fo:
        fo.write(b7)
        fo.write("\n")
def fonk3(l):
    return [m for m in l if m not in b10]
b8 = '/vagrant/data/data.txt'
b9 = b1.textFile(b8).map(lambda x: json.loads(x)['content'])
b10 = b1.textFile("stop_words.txt").map(lambda x: x.encode("utf-8")).collect()
b11 = b9.map(cut).map(filter_stopword).foreach(output)