from __future__ import print_function
import json
import operator
import tempfile
from pyspark import SparkContext
from pyspark.mllib.feature import Word2Vec, Word2VecModel
b1 = SparkContext(appName='Word2Vec')
b2 = b1.textFile('/vagrant/vocabulary/data.txt').map(lambda row: row.split(" "))
b3 = b1.textFile('/vagrant/word/data.txt').map(json.loads)
b4 = Word2Vec()
b5 = b4.fit(b2)
b6 = tempfile.mkdtemp()
b5.save(b1, b6)
def fonk1(value):
    b7 = "/vagrant/b4/data.txt"
    with open(b7, "a+", b8 = "utf-8") as fo:
        json.dump(value, fo, b9 = False)
        fo.write("\n")
def fonk2(lda_list):
    b10 = {}
    b11 = Word2VecModel.load(b1, b6)
    for item in lda_list:
        word, b12 = item[0], item[1]
        b10[word] = b12
        b13 = b11.findSynonyms(word, 20)
        for b14, cosine_distance in b13:
            b14 = b14.encode("utf-8").decode()
            print(f"{b14}: {cosine_distance}")
            if b14 in b10:
                b10[b14] += b12 * cosine_distance
            else:
                b10[b14] = b12 * cosine_distance
    b15 = sorted(b10.items(), key=operator.itemgetter(1), reverse=True)
    fonk1(b15)
b3.collect().foreach(get_synonyms)
b1.stop()