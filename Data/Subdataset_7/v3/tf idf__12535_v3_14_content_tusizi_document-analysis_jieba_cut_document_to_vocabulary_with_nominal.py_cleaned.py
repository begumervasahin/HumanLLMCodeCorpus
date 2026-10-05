import json
import jieba.posseg as pseg
from pyspark import SparkContext
b1 = SparkContext(appName='CutDocument')
def fonk1(text):
    b2 = pseg.cut(text)
    b3 = ["n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", "nsf", "nt", "nz", "nl", "ng", "s", "f", "v", "vd", "vn", "vf",
                   "vx", "vi", "vl", "vga", "ad", "an", "ag", "al"]
    b4 = [token.word.encode("utf-8") for token in b2 if token.flag in b3]
    return b4
def fonk2(tokens):
    b5 = "/vagrant/vocabulary/mominal.txt"
    b6 = " ".join(tokens)
    with open(b5, "a+") as file:
        file.write(b6 + "\n")
def fonk3(tokens):
    return [token for token in tokens if token not in b9]
b7 = '/vagrant/data/data.txt'
b8 = b1.textFile(b7).map(lambda x: json.loads(x)['content'])
b9 = b1.textFile("stop_words.txt").map(lambda word: word.encode("utf-8")).collect()
b10 = b8.flatMap(tokenize_text).filter(filter_stop_words).foreachPartition(write_tokens_to_file)
b1.stop()