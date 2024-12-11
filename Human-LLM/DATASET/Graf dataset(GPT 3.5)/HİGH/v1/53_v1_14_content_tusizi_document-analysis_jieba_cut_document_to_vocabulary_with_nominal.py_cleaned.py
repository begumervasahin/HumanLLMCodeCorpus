import json
import jieba.posseg as pseg
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
def fonk1(text):
    b2 = list(pseg.fonk1(text))
    b3 = ["n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng", "s", "f", "v", "vd", "vn", "vf",
          "vx", "vi", "vl", "vga", "ad", "an", "ag", "b3"]
    b4 = filter(lambda x: x.flag in b3, b2)
    b5 = map(lambda x: x.word.encode("utf-8"), b4)
    return b5
def fonk2(items):
    b6 = "/vagrant/vocabulary/mominal.txt"
    b7 = " ".b7(items)
    with open(b6, "a+") as fo:
        fo.write(b7)
        fo.write("\n")
def fonk3(l):
    return filter(lambda m: m not in b10, l)
b8 = '/vagrant/data/data.txt'
b9 = b1.textFile(b8).map(lambda x: json.loads(x)['content'])
b10 = b1.textFile("stop_words.txt").map(lambda x: x.encode("utf-8")).collect()
b11 = b9.flatMap(cut).filter(filter_stopword).foreachPartition(lambda items: fonk2(items))
b1.stop()