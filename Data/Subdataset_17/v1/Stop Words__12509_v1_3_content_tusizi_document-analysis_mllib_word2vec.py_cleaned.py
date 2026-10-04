from __future__ import print_function
import json
import operator
import tempfile
from pyspark import SparkContext
from pyspark.mllib.feature import Word2Vec
from pyspark.mllib.feature import Word2VecModel
sc = SparkContext(appName='Word2Vec')
vocabulary_rdd = sc.textFile('/vagrant/vocabulary/data.txt').map(lambda row: row.split(" "))
lda_rdd = sc.textFile('/vagrant/word/data.txt').map(json.loads)
word2vec = Word2Vec()
model = word2vec.fit(vocabulary_rdd)
temp_path = tempfile.mkdtemp()
model.save(sc, temp_path)
def output(value):
    filename = "/vagrant/word2vec/data.txt"
    with open(filename, "a+", encoding="utf-8") as fo:
        json.dump(value, fo, ensure_ascii=False)
        fo.write("\n")
def get_synonyms(lda_list):
    word_dict = {}
    same_model = Word2VecModel.load(sc, temp_path)
    for item in lda_list:
        word, weight = item[0], item[1]
        word_dict[word] = weight
        synonyms = same_model.findSynonyms(word, 20)
        for synonym, cosine_distance in synonyms:
            synonym = synonym.encode("utf-8").decode()
            print(f"{synonym}: {cosine_distance}")
            if synonym in word_dict:
                word_dict[synonym] += weight * cosine_distance
            else:
                word_dict[synonym] = weight * cosine_distance
    sorted_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    output(sorted_dict)
lda_rdd.collect().foreach(lambda x: get_synonyms(x))
sc.stop()