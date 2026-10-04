from __future__ import print_function
import json
import operator
import tempfile
from pyspark import SparkContext
from pyspark.mllib.feature import Word2Vec
from pyspark.mllib.feature import Word2VecModel
def fonk1(app_name):
    return SparkContext(b1 = app_name)
def fonk2(b13, b14, b15):
    b2 = b13.textFile(b14).map(lambda row: row.split(" "))
    b3 = b13.textFile(b15).map(json.loads)
    return b2, b3
def fonk3(b2):
    b4 = Word2Vec()
    return b4.fit(b2)
def fonk4(b9, b13):
    b5 = tempfile.mkdtemp()
    b9.save(b13, b5)
    return b5
def fonk5(value, filename):
    with open(filename, "a+", b6 = "utf-8") as file:
        b7 = json.dumps(value, ensure_ascii=False)
        file.write(b7 + "\n")
def fonk6(lda_list, b16, b13):
    b8 = {}
    b9 = Word2VecModel.load(b13, b16)
    for word, weight in lda_list:
        b8[word] = weight
        b10 = b9.findSynonyms(word, 20)
        for b11, cosine_distance in b10:
            b11 = b11.encode("utf-8")
            print(f"{b11}: {cosine_distance}")
            if b11 in b8:
                b8[b11] += weight * cosine_distance
            else:
                b8[b11] = weight * cosine_distance
    b12 = sorted(b8.items(), key=operator.itemgetter(1), reverse=True)
    fonk5(b12, "/vagrant/b4/data.txt")
def fonk7():
    b13 = fonk1('Word2Vec')
    b14 = '/vagrant/vocabulary/data.txt'
    b15 = '/vagrant/word/data.txt'
    b2, b3 = fonk2(b13, b14, b15)
    b9 = fonk3(b2)
    b16 = fonk4(b9, b13)
    b17 = b3.collect()
    for lda_list in b17:
        fonk6(lda_list, b16, b13)
    b13.stop()
if b18 = = "__main__":
    fonk7()