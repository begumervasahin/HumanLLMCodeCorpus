import json
import jieba
from pyspark import SparkContext
sc = SparkContext(appName='CutDocument')
def encode_to_utf8(text):
    return text.encode("utf-8")
def cut_text(text):
    seg_list = jieba.cut(text, cut_all=False)
    filtered_list = (word for word in seg_list if word and not isinstance(word, float))
    encoded_list = map(encode_to_utf8, filtered_list)
    return list(encoded_list)
def save_to_file(items, filename="/vagrant/result/jieba_cut_word.txt"):
    with open(filename, "a+") as file:
        file.write(" ".join(items))
        file.write("\n")
src_file = '/vagrant/data/data.txt'
rdd = sc.textFile(src_file).map(lambda x: json.loads(x)['content'])
stop_word_file = "stop_words.txt"
stop_words = set(sc.textFile(stop_word_file).map(encode_to_utf8).collect())
def filter_stop_words(word_list):
    return [word for word in word_list if word not in stop_words]
cut_word_rdd = rdd.map(cut_text)
filtered_rdd = cut_word_rdd.map(filter_stop_words)
filtered_rdd.foreach(save_to_file)