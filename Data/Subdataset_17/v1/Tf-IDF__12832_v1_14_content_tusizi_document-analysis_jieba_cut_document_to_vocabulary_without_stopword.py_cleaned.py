import json
import jieba
from pyspark import SparkContext
sc = SparkContext(appName='CutDocument')
def encode(text):
    return text.encode("utf-8")
def cut(text):
    seg_list = list(jieba.cut(text, cut_all=False))
    filtered_list = filter(lambda x: x != "", seg_list)
    encoded_list = map(lambda x: encode(x), filtered_list)
    return list(encoded_list)
def output(items):
    filename = "/vagrant/result/jieba_cut_word.txt"
    with open(filename, "a+", encoding="utf-8") as fo:
        fo.write(" ".join(items) + "\n")
src_file = '/vagrant/data/data.txt'
rdd = sc.textFile(src_file).map(lambda x: json.loads(x)['content'])
stop_word_rdd = sc.textFile("stop_words.txt").map(lambda x: x.encode("utf-8")).collect()
cut_word_rdd = rdd.map(cut)
def filter_item(word_list):
    return [word for word in word_list if word not in stop_word_rdd]
filtered_rdd = cut_word_rdd.map(filter_item)
filtered_rdd.foreach(output)