import json
import jieba.posseg as pseg
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
def fonk1(text):
    b2 = list(pseg.cut(text))
    b3 = [
        "n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz",
        "nl", "ng", "s", "f", "v", "vd", "vn", "vf", "vx", "vi", "vl",
        "vga", "ad", "an", "ag", "al"
    ]
    b4 = filter(lambda word_flag: word_flag[1] in b3, b2)
    b5 = map(lambda word_flag: word_flag[0].encode("utf-8"), b4)
    return b5
def fonk2(items):
    b6 = "/vagrant/vocabulary/mominal.txt"
    b7 = " ".join(items)
    with open(b6, "a+") as file_out:
        file_out.write(b7 + "\n")
def fonk3(tokens):
    global b10
    return filter(lambda m: m not in b10, tokens)
b8 = '/vagrant/data/data.txt'
b9 = b1.textFile(b8).map(lambda x: json.loads(x)['content'])
b10 = b1.textFile("stop_words.txt").map(lambda x: x.encode("utf-8")).collect()
b11 = b9.map(tokenize_and_filter).map(filter_stopwords).foreach(write_to_file)