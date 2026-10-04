import json
import jieba
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
def fonk1(text):
    return text.encode("utf-8")
def fonk2(text):
    b2 = jieba.cut(text, cut_all=False)
    b3 = [seg for seg in b2 if seg != ""]
    b4 = [fonk1(seg) for seg in b3]
    return b4
def fonk3(items):
    b5 = "/vagrant/result/jieba_cut_word.txt"
    with open(b5, "a+", b6 = "utf-8") as file:
        file.write(" ".join(items) + "\n")
def fonk4(word_list, b9):
    return [word for word in word_list if word not in b9]
def fonk5():
    b7 = '/vagrant/data/data.txt'
    b8 = b1.textFile(b7).map(lambda x: json.loads(x)['content'])
    b9 = b1.textFile("b9.txt").map(lambda x: x.encode("utf-8")).collect()
    b10 = b8.map(cut_and_encode)
    b11 = b10.map(lambda word_list: fonk4(word_list, b9))
    b11.foreach(write_to_file)
if b12 = = "__main__":
    fonk5()