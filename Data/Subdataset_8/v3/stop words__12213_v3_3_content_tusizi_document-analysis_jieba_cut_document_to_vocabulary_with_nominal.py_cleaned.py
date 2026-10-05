import json
import jieba.posseg as pseg
from pyspark import SparkContext
sc = SparkContext(appName='CutDocument')
def tokenize_and_filter(text):
    seg_list = list(pseg.cut(text))
    allowed_flags = [
        "n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz",
        "nl", "ng", "s", "f", "v", "vd", "vn", "vf", "vx", "vi", "vl",
        "vga", "ad", "an", "ag", "al"
    ]
    filtered_list = filter(lambda word_flag: word_flag[1] in allowed_flags, seg_list)
    encoded_tokens = [word_flag[0].encode("utf-8") for word_flag in filtered_list]
    return encoded_tokens
def write_to_file(items):
    filename = "/vagrant/vocabulary/mominal.txt"
    joined_words = " ".join(items)
    with open(filename, "a+") as file_out:
        file_out.write(joined_words + "\n")
def filter_stopwords(tokens):
    global stopWordRdd
    return filter(lambda m: m not in stopWordRdd, tokens)
src_file = '/vagrant/data/data.txt'
rdd = sc.textFile(src_file).map(lambda x: json.loads(x)['content'])
stopWordRdd = set(sc.textFile("stop_words.txt").map(lambda x: x.strip().encode("utf-8")).collect())
result = rdd.map(tokenize_and_filter).map(filter_stopwords).foreach(write_to_file)