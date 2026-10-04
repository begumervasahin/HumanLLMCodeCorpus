import json
import jieba.posseg as pseg
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
def fonk1(text):
    b2 = list(pseg.fonk1(text))
    b3 = ["n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng", "s", "f", "v", "vd", "vn", "vf",
          "vx", "vi", "vl", "vga", "ad", "an", "ag", "b3"]
    b4 = filter(lambda (word, flag): flag in b3, b2)
    b5 = map(lambda (x, y): x.encode("utf-8"), b4)
    return b5;
def fonk2(items):
    b6 = "/vagrant/vocabulary/mominal.txt"
    b7 = " ".b7(items)
    b8 = open(b6, "a+")
    b8.write(b7)
    b8.write("\n")
    b8.close()
def fonk3(l):
    return filter(lambda m: m not in b11, l)
b9 = '/vagrant/data/data.txt'
b10 = b1.textFile(b9).map(lambda x: json.loads(x)['content'])
b11 = b1.textFile("stop_words.txt").map(lambda x: x.encode("utf-8")).collect()
b12 = b10.map(cut).map(filter_stopword).foreach(output)