import json
import jieba.posseg as pseg
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
def fonk1(text):
    b2 = list(pseg.cut(text))
    b3 = ["n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng",
                     "s", "f", "v", "vd", "vn", "vf", "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"]
    b4 = filter(lambda word_flag: word_flag[1] in b3, b2)
    b5 = map(lambda word_flag: word_flag[0].encode("utf-8"), b4)
    return b5
def fonk2(items, filename):
    b6 = " ".join(items)
    with open(filename, "a+") as fo:
        fo.write(b6)
        fo.write("\n")
def fonk3(word_list, b9):
    return filter(lambda word: word not in b9, word_list)
b7 = '/vagrant/data/data.txt'
b8 = 'b9.txt'
b9 = b1.textFile(b8).map(lambda x: x.encode("utf-8")).collect()
b10 = b1.textFile(b7).map(lambda x: json.loads(x)['content'])
b11 = b10.map(tokenize_and_filter).map(lambda x: fonk3(x, b9)) \
            .foreach(lambda x: fonk2(x, "/vagrant/vocabulary/mominal.txt"))
b1.stop()