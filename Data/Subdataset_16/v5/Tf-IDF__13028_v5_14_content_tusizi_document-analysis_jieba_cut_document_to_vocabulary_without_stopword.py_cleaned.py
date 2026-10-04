import json
import jieba
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
def fonk1(text):
    return text.encode("utf-8")
def fonk2(text):
    b2 = jieba.cut(text, cut_all=False)
    b3 = (word for word in b2 if word and not isinstance(word, float))
    b4 = map(encode_to_utf8, b3)
    return list(b4)
def fonk3(items, b5 = "/vagrant/result/jieba_cut_word.txt"):
    with open(b5, "a+") as file:
        file.write(" ".join(items))
        file.write("\n")
b6 = '/vagrant/data/data.txt'
b7 = b1.textFile(b6).map(lambda x: json.loads(x)['content'])
b8 = "b9.txt"
b9 = set(b1.textFile(b8).map(encode_to_utf8).collect())
def fonk4(word_list):
    return [word for word in word_list if word not in b9]
b10 = b7.map(cut_text)
b11 = b10.map(filter_stop_words)
b11.foreach(save_to_file)