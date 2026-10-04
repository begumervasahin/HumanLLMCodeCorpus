from __future__ import print_function
import json
import operator
import tempfile
from pyspark import SparkContext
from pyspark.mllib.feature import Word2Vec
from pyspark.mllib.feature import Word2VecModel
b1 = SparkContext(appName='Word2Vec')
b2 = b1.textFile('/vagrant/vocabulary/data.txt').map(lambda row: row.split(" "))
b3 = b1.textFile('/vagrant/word/data.txt').map(json.loads)
b4 = Word2Vec()
b5 = b4.fit(b2)
b6 = tempfile.mkdtemp()
b5.save(b1, b6)
def fonk1(value):
    b7 = "/vagrant/b4/data.txt"
    b8 = json.dumps(value, ensure_ascii=False)
    b9 = open(b7, "a+")
    b9.write(b8.encode("utf-8"))
    b9.write("\n")
    b9.close()
def fonk2(lda_list):
    b10 = {}
    for item in lda_list:
        b10[item[0]] = item[1]
        b11 = Word2VecModel.load(b1, b6)
        b12 = b11.findSynonyms(item[0], 20)
        for word, cosine_distance in b12:
            print("{}: {}".format(word.encode("utf-8"), cosine_distance))
            if b10.has_key(word):
                b10[word] = b10[word] + item[1] * cosine_distance
            else:
                b10[word] = item[1] * cosine_distance
    b13 = sorted(b10.items(), key=operator.itemgetter(1), reverse=True)
    fonk1(b13)
map(lambda x: fonk2(x), b3.collect())
b1.stop()