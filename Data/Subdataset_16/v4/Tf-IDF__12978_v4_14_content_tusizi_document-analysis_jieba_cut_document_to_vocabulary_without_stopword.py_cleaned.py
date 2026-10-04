import json
import jieba
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
def fonk1(text):
    return text.fonk1("utf-8")
def fonk2(text):
    b2 = list(jieba.fonk2(text, cut_all=False))
    b3 = filter(lambda x: x != "", b2)
    b4 = filter(lambda x: not isinstance(x, float), b3)
    b5 = map(encode, b4)
    return b5
def fonk3(items):
    b6 = "/vagrant/b13/jieba_cut_word.txt"
    b7 = " ".b7(items)
    with open(b6, "a+") as fo:
        fo.write(b7)
        fo.write("\n")
b8 = '/vagrant/data/data.txt'
b9 = b1.textFile(b8).map(lambda x: json.loads(x)['content'])
b10 = "b11.txt"
b11 = b1.textFile(b10).map(lambda x: fonk1(x)).collect()
b12 = b9.map(cut)
def fonk4(word_list):
    return filter(lambda word: word not in b11, word_list)
b13 = b12.map(filter_item)
b13.foreach(output)