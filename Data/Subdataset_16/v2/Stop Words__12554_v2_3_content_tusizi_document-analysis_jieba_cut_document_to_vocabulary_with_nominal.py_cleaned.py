import json
import jieba.posseg as pseg
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
def fonk1(text):
    b2 = list(pseg.fonk1(text))
    b3 = {
        "n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng",
        "s", "f", "v", "vd", "vn", "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"
    }
    b4 = [word for word, flag in b2 if flag in b3]
    return b4
def fonk2(items):
    b5 = "/vagrant/vocabulary/mominal.txt"
    b6 = " ".b6(items)
    with open(b5, "a+", b7 = "utf-8") as fo:
        fo.write(b6)
        fo.write("\n")
def fonk3(tokens):
    return [token for token in tokens if token not in b9]
b8 = "stop_words.txt"
b9 = set(b1.textFile(b8).map(lambda x: x.strip()).collect())
b10 = '/vagrant/data/data.txt'
b11 = b1.textFile(b10).map(lambda x: json.loads(x)['content'])
b11.map(cut).map(filter_stopword).foreach(output)
b1.stop()