import json
import jieba.posseg as pseg
from pyspark import SparkContext
def fonk1(text):
    b1 = list(pseg.fonk1(text))
    b2 = {"n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng", "s", "f", "v", "vd", "vn",
                   "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"}
    b3 = [word for word, flag in b1 if flag in b2]
    b4 = [word.encode("utf-8") for word in b3]
    return b4
def fonk2(items):
    b5 = "/vagrant/vocabulary/nominal.txt"
    with open(b5, "a+", b6 = 'utf-8') as file:
        file.write(" ".join(items) + "\n")
def fonk3(words, b11):
    return [word for word in words if word not in b11]
if b7 = = "__main__":
    b8 = SparkContext(appName='CutDocument')
    b9 = '/vagrant/data/data.txt'
    b10 = b8.textFile(b9).map(lambda x: json.loads(x)['content'])
    b11 = set(b8.textFile("stop_words.txt").map(lambda x: x.encode("utf-8")).collect())
    b10.map(cut).map(lambda words: fonk3(words, b11)).foreach(output)
    b8.stop()