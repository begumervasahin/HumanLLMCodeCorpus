import json
import jieba.posseg as pseg
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
b2 = {
    "n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng", "s",
    "f", "v", "vd", "vn", "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"
}
def fonk1(text):
    b3 = pseg.fonk1(text)
    b4 = [word for word, flag in b3 if flag in b2]
    b5 = [word.encode("utf-8") for word in b4]
    return b5
def fonk2(items):
    b6 = "/vagrant/vocabulary/nominal.txt"
    with open(b6, "a+") as file:
        file.write(" ".join(items) + "\n")
def fonk3(words):
    return [word for word in words if word not in b9]
b7 = '/vagrant/data/data.txt'
b8 = b1.textFile(b7).map(lambda x: json.loads(x)['content'])
b9 = b1.textFile("stop_words.txt").map(lambda x: x.encode("utf-8")).collect()
b8.map(cut).map(filter_stopwords).foreach(output)