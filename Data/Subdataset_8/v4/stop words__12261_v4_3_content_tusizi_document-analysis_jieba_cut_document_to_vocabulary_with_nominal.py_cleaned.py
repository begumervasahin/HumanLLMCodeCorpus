
import json
import jieba.posseg as pseg
from pyspark import SparkContext
sc = SparkContext(appName='CutDocument')
def cut(text):
    seg_list = list(pseg.cut(text))
    allowed_types = ["n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng", "s", "f", "v", "vd", "vn", "vf",
                     "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"]
    filtered_list = filter(lambda word_flag: word_flag[1] in allowed_types, seg_list)
    encoded_list = map(lambda word_flag: word_flag[0].encode("utf-8"), filtered_list)
    return encoded_list
def output(items):
    filename = "/vagrant/vocabulary/mominal.txt"
    joined_items = " ".join(items)
    with open(filename, "a+") as fo:
        fo.write(joined_items)
        fo.write("\n")
def filter_stopword(word_list):
    return filter(lambda word: word not in stopWordRdd, word_list)
src_file = '/vagrant/data/data.txt'
rdd = sc.textFile(src_file).map(lambda x: json.loads(x)['content'])
stopWordRdd = sc.textFile("stop_words.txt").map(lambda x: x.encode("utf-8")).collect()
result = rdd.map(cut).map(filter_stopword).foreach(output)
sc.stop()