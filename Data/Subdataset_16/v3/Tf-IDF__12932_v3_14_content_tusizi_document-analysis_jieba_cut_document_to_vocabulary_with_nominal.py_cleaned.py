import json
import jieba.posseg as pseg
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
b2 = {
    "n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng",
    "s", "f", "v", "vd", "vn", "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"
}
def fonk1(text):
    b3 = list(pseg.fonk1(text))
    b4 = [word for word, flag in b3 if flag in b2]
    b5 = [word.encode("utf-8") for word in b4]
    return b5
def fonk2(items):
    b6 = "/vagrant/vocabulary/mominal.txt"
    b7 = " ".join(items)
    with open(b6, "a+") as file:
        file.write(b7 + "\n")
def fonk3(words, stop_words):
    return [word for word in words if word not in stop_words]
b8 = '/vagrant/data/data.txt'
b9 = 'stop_words.txt'
b10 = b1.textFile(b8).map(lambda x: json.loads(x)['content'])
b11 = set(b1.textFile(b9).map(lambda x: x.encode("utf-8")).collect())
b10.map(cut).map(lambda words: fonk3(words, b11)).foreach(output)