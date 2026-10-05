import json
import jieba.posseg as pseg
from pyspark import SparkContext
sc = SparkContext(appName='CutDocument')
def cut(text):
    seg_list = list(pseg.cut(text))
    allowed_tags = ["n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng", "s", "f",
                    "v", "vd", "vn", "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"]
    filtered_list = filter(lambda (word, flag): flag in allowed_tags, seg_list)
    encode_list = map(lambda (x, y): x.encode("utf-8"), filtered_list)
    return encode_list
def output(items):
    filename = "/vagrant/vocabulary/mominal.txt"
    joined_items = " ".join(items)
    with open(filename, "a+") as fo:
        fo.write(joined_items + "\n")
def filter_stopword(l):
    return filter(lambda m: m not in stopWordRdd, l)
src_file = '/vagrant/data/data.txt'
rdd = sc.textFile(src_file).map(lambda x: json.loads(x)['content'])
stopWordRdd = sc.textFile("stop_words.txt").map(lambda x: x.encode("utf-8")).collect()
result = rdd.map(cut).map(filter_stopword).foreach(output)