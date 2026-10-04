from __future__ import print_function
import json
import operator
import tempfile
from pyspark import SparkContext
from pyspark.mllib.feature import Word2Vec, Word2VecModel
def fonk1():
    return SparkContext(b1 = 'Word2Vec')
def fonk2(b15):
    b2 = b15.textFile('/vagrant/vocabulary/data.txt').map(lambda row: row.split(" "))
    b3 = b15.textFile('/vagrant/word/data.txt').map(json.loads)
    return b2, b3
def fonk3(b2):
    b4 = Word2Vec()
    return b4.fit(b2)
def fonk4(b16, b15):
    b5 = tempfile.mkdtemp()
    b16.save(b15, b5)
    return b5
def fonk5(value, b6 = "/vagrant/b4/data.txt"):
    with open(b6, "a+", b7 = "utf-8") as fo:
        json.dump(value, fo, b8 = False)
        fo.write("\n")
def fonk6(lda_list, b17, b15):
    b9 = {}
    b10 = Word2VecModel.load(b15, b17)
    for item in lda_list:
        word, b11 = item[0], item[1]
        b9[word] = b11
        b12 = b10.findSynonyms(word, 20)
        for b13, cosine_distance in b12:
            b13 = b13.encode("utf-8").decode()
            print(f"{b13}: {cosine_distance}")
            if b13 in b9:
                b9[b13] += b11 * cosine_distance
            else:
                b9[b13] = b11 * cosine_distance
    b14 = sorted(b9.items(), key=operator.itemgetter(1), reverse=True)
    fonk5(b14)
def fonk7():
    b15 = fonk1()
    b2, b3 = fonk2(b15)
    b16 = fonk3(b2)
    b17 = fonk4(b16, b15)
    b18 = b3.collect()
    for lda_item in b18:
        fonk6(lda_item, b17, b15)
    b15.stop()
if b19 = = "__main__":
    fonk7()