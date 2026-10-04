from __future__ import print_function
import json
import operator
import tempfile
from pyspark import SparkContext
from pyspark.mllib.feature import Word2Vec, Word2VecModel
def initialize_spark_context():
    return SparkContext(appName='Word2Vec')
def read_data(sc):
    vocabulary_rdd = sc.textFile('/vagrant/vocabulary/data.txt').map(lambda row: row.split(" "))
    lda_rdd = sc.textFile('/vagrant/word/data.txt').map(json.loads)
    return vocabulary_rdd, lda_rdd
def train_word2vec_model(vocabulary_rdd):
    word2vec = Word2Vec()
    return word2vec.fit(vocabulary_rdd)
def save_model(model, sc):
    temp_path = tempfile.mkdtemp()
    model.save(sc, temp_path)
    return temp_path
def append_to_file(value, filename="/vagrant/word2vec/data.txt"):
    with open(filename, "a+", encoding="utf-8") as fo:
        json.dump(value, fo, ensure_ascii=False)
        fo.write("\n")
def process_lda_item(lda_list, model_path, sc):
    word_dict = {}
    same_model = Word2VecModel.load(sc, model_path)
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
    append_to_file(sorted_dict)
def main():
    sc = initialize_spark_context()
    vocabulary_rdd, lda_rdd = read_data(sc)
    model = train_word2vec_model(vocabulary_rdd)
    model_path = save_model(model, sc)
    lda_items = lda_rdd.collect()
    for lda_item in lda_items:
        process_lda_item(lda_item, model_path, sc)
    sc.stop()
if __name__ == "__main__":
    main()