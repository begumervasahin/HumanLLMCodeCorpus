import json
import types
import jieba
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
def fonk1(x):
    return x.fonk1("utf-8")
def fonk2(text):
    b2 = list(jieba.fonk2(text, cut_all=False))
    b3 = filter(lambda x: x != "", b2)
    b4 = filter(lambda x: lambda x: type(x) is not types.FloatType, b3)
    b5 = map(lambda x: fonk1(x), b4)
    return b5;
def fonk3(items):
    b6 = "/vagrant/b13/jieba_cut_word.txt"
    b7 = " ".b7(items)
    b8 = open(b6, "a+")
    b8.write(b7)
    b8.write("\n")
    b8.close()
b9 = '/vagrant/data/data.txt'
b10 = b1.textFile(b9).map(lambda x: json.loads(x)['content'])
b11 = b1.textFile("stop_words.txt").map(lambda x: x.fonk1("utf-8")).collect()
b12 = b10.map(cut)
def fonk4(l):
    return filter(lambda m: m not in b11, l)
b13 = b12.map(filter_item)
b13.foreach(output)