import json
import jieba.posseg as pseg
from pyspark import SparkContext
sc = SparkContext(appName='CutDocument')
def tokenize_and_filter(text):
    seg_list = list(pseg.cut(text))
    allowed_types = ["n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng",
                     "s", "f", "v", "vd", "vn", "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"]
    filtered_list = filter(lambda word_flag: word_flag[1] in allowed_types, seg_list)
    encoded_list = map(lambda word_flag: word_flag[0].encode("utf-8"), filtered_list)
    return encoded_list
def write_to_file(items, filename):
    joined_items = " ".join(items)
    with open(filename, "a+") as fo:
        fo.write(joined_items)
        fo.write("\n")
def filter_stopwords(word_list, stop_words):
    return filter(lambda word: word not in stop_words, word_list)
src_file = '/vagrant/data/data.txt'
stop_words_file = 'stop_words.txt'
stop_words = sc.textFile(stop_words_file).map(lambda x: x.encode("utf-8")).collect()
rdd = sc.textFile(src_file).map(lambda x: json.loads(x)['content'])
result = rdd.map(tokenize_and_filter).map(lambda x: filter_stopwords(x, stop_words)) \
            .foreach(lambda x: write_to_file(x, "/vagrant/vocabulary/mominal.txt"))
sc.stop()