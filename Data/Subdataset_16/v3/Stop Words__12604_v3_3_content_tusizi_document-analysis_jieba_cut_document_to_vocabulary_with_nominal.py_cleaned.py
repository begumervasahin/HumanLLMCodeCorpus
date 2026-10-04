import json
import jieba.posseg as pseg
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
def fonk1(text):
    b2 = pseg.fonk1(text)
    b3 = {
        "n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng",
        "s", "f", "v", "vd", "vn", "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"
    }
    b4 = [word for word, flag in b2 if flag in b3]
    return b4
def fonk2(items):
    b5 = "/vagrant/vocabulary/mominal.txt"
    with open(b5, "a+", b6 = "utf-8") as fo:
        fo.write(" ".join(items))
        fo.write("\n")
def fonk3(tokens):
    return [token for token in tokens if token not in b8]
b7 = "stop_words.txt"
b8 = set(b1.textFile(b7).map(lambda x: x.strip()).collect())
b9 = '/vagrant/data/data.txt'
b10 = b1.textFile(b9).map(lambda x: json.loads(x)['content'])
b10.map(cut).map(filter_stopwords).foreach(output)
b1.stop()