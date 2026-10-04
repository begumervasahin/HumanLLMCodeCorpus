import json
import jieba
from pyspark import SparkContext
sc = SparkContext(appName='CutDocument')
def encode(text):
    return text.encode("utf-8")
def cut(text):
    seg_list = list(jieba.cut(text, cut_all=False))
    filtered_list = filter(lambda x: x != "", seg_list)
    string_list = filter(lambda x: not isinstance(x, float), filtered_list)
    encode_list = map(encode, string_list)
    return encode_list
def output(items):
    filename = "/vagrant/result/jieba_cut_word.txt"
    join = " ".join(items)
    with open(filename, "a+") as fo:
        fo.write(join)
        fo.write("\n")
src_file = '/vagrant/data/data.txt'
rdd = sc.textFile(src_file).map(lambda x: json.loads(x)['content'])
stop_word_file = "stop_words.txt"
stop_words = sc.textFile(stop_word_file).map(lambda x: encode(x)).collect()
cut_word_rdd = rdd.map(cut)
def filter_item(word_list):
    return filter(lambda word: word not in stop_words, word_list)
result = cut_word_rdd.map(filter_item)
result.foreach(output)