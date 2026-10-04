import json
import jieba
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
def fonk1(text):
    return text.encode("utf-8")
def fonk2(text):
    b2 = jieba.cut(text, cut_all=False)
    b3 = filter(lambda x: x != "", b2)
    b4 = map(encode_text, b3)
    return list(b4)
def fonk3(items):
    b5 = "/vagrant/result/jieba_cut_word.txt"
    with open(b5, "a+", b6 = "utf-8") as file:
        file.write(" ".join(items) + "\n")
b7 = '/vagrant/data/data.txt'
b8 = b1.textFile(b7).map(lambda x: json.loads(x)['content'])
b9 = b1.textFile("b9.txt").map(lambda x: x.encode("utf-8")).collect()
def fonk4(word_list):
    return [word for word in word_list if word not in b9]
b10 = b8.map(cut_and_encode)
b11 = b10.map(filter_stop_words)
b11.foreach(write_to_file)