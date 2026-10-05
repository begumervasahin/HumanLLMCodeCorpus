import json
import jieba.posseg as pseg
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
def fonk1(text):
    b2 = list(pseg.cut(text))
    b3 = ["n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng", "s", "f",
                    "v", "vd", "vn", "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"]
    b4 = [word for word, flag in b2 if flag in b3]
    b5 = [word.encode("utf-8") for word in b4]
    return b5
def fonk2(items):
    b6 = "/vagrant/vocabulary/mominal.txt"
    b7 = " ".join(items)
    with open(b6, "a+") as file:
        file.write(b7 + "\n")
def fonk3(words):
    return [word for word in words if word not in b10]
b8 = '/vagrant/data/data.txt'
b9 = b1.textFile(b8).map(lambda x: json.loads(x)['content'])
b10 = set(b1.textFile("b10.txt").map(lambda x: x.strip().encode("utf-8")).collect())
b11 = b9.map(tokenize_and_filter).map(filter_stopwords).foreach(write_to_file)